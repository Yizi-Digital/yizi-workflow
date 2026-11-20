#!/usr/bin/env python3
"""Descarga los modelos de Yizi Voz Local a ./models y verifica sus sumas SHA-256.

Uso:
    python scripts/descargar_modelos.py                  # paquetes por defecto
    python scripts/descargar_modelos.py --paquete whisper-large-v3-turbo
    python scripts/descargar_modelos.py --solo-verificar  # no descarga nada
    python scripts/descargar_modelos.py --listar

Solo usa la biblioteca estandar de Python. Respeta HTTPS_PROXY y SSL_CERT_FILE.
Si un archivo ya existe y su suma coincide, no se descarga otra vez.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import ssl
import sys
import time
import urllib.request
from pathlib import Path

RAIZ = Path(os.environ.get("YIZI_VOZ_DIR") or Path(__file__).resolve().parent.parent)
MANIFIESTO = Path(__file__).resolve().parent / "modelos.json"
BLOQUE = 1024 * 1024


def contexto_ssl() -> ssl.SSLContext:
    """Usa SSL_CERT_FILE si existe; si no, certifi si esta instalado; si no, el del sistema."""
    if os.environ.get("SSL_CERT_FILE"):
        return ssl.create_default_context(cafile=os.environ["SSL_CERT_FILE"])
    try:
        import certifi  # viene con httpx

        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def sha256_de(ruta: Path) -> str:
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for trozo in iter(lambda: f.read(BLOQUE), b""):
            h.update(trozo)
    return h.hexdigest()


def es_mac_arm64() -> bool:
    return sys.platform == "darwin" and platform.machine() == "arm64"


def archivo_valido(ruta: Path, info: dict) -> tuple[bool, str]:
    if not ruta.exists():
        return False, "falta"
    if info.get("tamano") and ruta.stat().st_size != info["tamano"]:
        return False, f"tamano {ruta.stat().st_size} != {info['tamano']}"
    if info.get("sha256"):
        suma = sha256_de(ruta)
        if suma != info["sha256"]:
            return False, f"suma distinta ({suma[:12]}...)"
        return True, "suma OK"
    return True, "sin suma fijada en el manifiesto (solo tamano)"


def descargar(url: str, destino: Path, ctx: ssl.SSLContext) -> None:
    parcial = destino.with_suffix(destino.suffix + ".part")
    inicio = parcial.stat().st_size if parcial.exists() else 0
    peticion = urllib.request.Request(url, headers={"User-Agent": "yizi-voz-local/1.0"})
    if inicio:
        peticion.add_header("Range", f"bytes={inicio}-")
    abridor = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ctx))
    with abridor.open(peticion, timeout=60) as resp:
        if inicio and resp.status != 206:
            inicio = 0  # el servidor no admite reanudar
        total = resp.length + inicio if resp.length else None
        modo = "ab" if inicio else "wb"
        hecho = inicio
        ultimo = 0.0
        with parcial.open(modo) as f:
            while True:
                trozo = resp.read(BLOQUE)
                if not trozo:
                    break
                f.write(trozo)
                hecho += len(trozo)
                ahora = time.time()
                if ahora - ultimo > 2:
                    ultimo = ahora
                    if total:
                        print(f"    {hecho / 1e6:8.1f} / {total / 1e6:.1f} MB", flush=True)
    parcial.replace(destino)


def procesar(nombre: str, paquete: dict, solo_verificar: bool, ctx: ssl.SSLContext) -> bool:
    destino = RAIZ / paquete["destino"]
    destino.mkdir(parents=True, exist_ok=True)
    print(f"[{nombre}] {paquete['descripcion']}")
    todo_ok = True
    for info in paquete["archivos"]:
        ruta = destino / info["nombre"]
        ok, motivo = archivo_valido(ruta, info)
        if ok:
            print(f"  OK  {info['nombre']} ({motivo})")
            continue
        if solo_verificar:
            print(f"  MAL {info['nombre']}: {motivo}")
            todo_ok = False
            continue
        print(f"  ... descargando {info['nombre']} ({motivo})")
        if ruta.exists():
            ruta.unlink()
        try:
            descargar(info["url"], ruta, ctx)
        except Exception as e:  # red, proxy o servidor
            print(f"  ERROR al descargar {info['nombre']}: {e}")
            todo_ok = False
            continue
        ok, motivo = archivo_valido(ruta, info)
        if not ok:
            print(f"  ERROR {info['nombre']}: {motivo}. Borro el archivo; vuelve a intentarlo.")
            ruta.unlink(missing_ok=True)
            todo_ok = False
        else:
            print(f"  OK  {info['nombre']} ({motivo})")
    return todo_ok


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--paquete", action="append", help="Nombre del paquete (se puede repetir)")
    p.add_argument("--solo-verificar", action="store_true", help="No descarga; solo comprueba")
    p.add_argument("--listar", action="store_true", help="Muestra los paquetes y sale")
    args = p.parse_args()

    manifiesto = json.loads(MANIFIESTO.read_text(encoding="utf-8"))["paquetes"]
    if args.listar:
        for nombre, paq in manifiesto.items():
            marca = "por defecto" if paq.get("por_defecto") else "opcional"
            print(f"{nombre:28} {marca:12} {paq['licencia']}\n    {paq['descripcion']}")
        return 0

    elegidos = args.paquete or [n for n, paq in manifiesto.items() if paq.get("por_defecto")]
    ctx = contexto_ssl()
    resultado = True
    for nombre in elegidos:
        if nombre not in manifiesto:
            print(f"Paquete desconocido: {nombre}. Usa --listar.")
            return 2
        paq = manifiesto[nombre]
        if paq.get("solo_mac_arm64") and not es_mac_arm64():
            print(f"[{nombre}] Se salta: solo sirve en Mac con Apple Silicon.")
            continue
        resultado = procesar(nombre, paq, args.solo_verificar, ctx) and resultado
    print("Listo." if resultado else "Hubo errores. Revisa los mensajes de arriba.")
    return 0 if resultado else 1


if __name__ == "__main__":
    sys.exit(main())
