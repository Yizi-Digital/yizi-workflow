"""Paso de texto en español a fonemas (G2P) para Kokoro, sin espeak-ng.

Por qué existe: kokoro-onnx usa espeak-ng y phonemizer para los fonemas, y los dos
son GPL-3.0. Este módulo es código propio de Yizi, con las reglas de la ortografía
española, que es casi fonética. Produce fonemas al estilo de espeak-ng
(acento ˈ justo antes de la vocal tónica), que es lo que vio Kokoro al entrenar.

Variante: español latinoamericano (seseo: c/z suenan /s/; ll y y suenan /ʝ/).
Limitaciones: palabras en inglés y siglas raras suenan "a la española". Para
corregir una palabra, añádela en config/pronunciacion.yaml.
"""
from __future__ import annotations

import re
import unicodedata

VOCALES = "aeiouáéíóúü"
FUERTES = "aeoáéó"
TILDES = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u"}

# Palabras átonas: espeak-ng no les pone acento.
ATONAS = {
    "el", "la", "los", "las", "lo", "un", "una", "unos", "unas", "de", "del", "al",
    "a", "en", "y", "e", "o", "u", "ni", "que", "se", "me", "te", "le", "les", "nos",
    "os", "mi", "mis", "tu", "tus", "su", "sus", "por", "con", "sin", "para", "pero",
    "si", "como", "cuando", "donde", "porque", "mas", "tan", "hasta", "desde", "sobre",
    "entre", "hacia", "según", "segun",
}

UNIDADES = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
            "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
            "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés",
            "veinticuatro", "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
DECENAS = ["", "", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
CENTENAS = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos",
            "seiscientos", "setecientos", "ochocientos", "novecientos"]

LETRAS = {"a": "a", "b": "be", "c": "se", "d": "de", "e": "e", "f": "efe", "g": "ge",
          "h": "ache", "i": "i", "j": "jota", "k": "ka", "l": "ele", "m": "eme", "n": "ene",
          "ñ": "eñe", "o": "o", "p": "pe", "q": "cu", "r": "erre", "s": "ese", "t": "te",
          "u": "u", "v": "uve", "w": "doble u", "x": "equis", "y": "ye", "z": "seta"}

SIMBOLOS = {"%": " por ciento", "&": " y ", "+": " más ", "=": " igual a ", "@": " arroba ",
            "€": " euros", "$": " dólares", "°": " grados", "#": " número "}


def numero_a_palabras(n: int) -> str:
    """Entero no negativo a palabras en español (hasta billones)."""
    if n < 30:
        return UNIDADES[n]
    if n < 100:
        d, u = divmod(n, 10)
        return DECENAS[d] + ("" if u == 0 else " y " + UNIDADES[u])
    if n == 100:
        return "cien"
    if n < 1000:
        c, r = divmod(n, 100)
        return CENTENAS[c] + ("" if r == 0 else " " + numero_a_palabras(r))
    if n < 1_000_000:
        m, r = divmod(n, 1000)
        pre = "mil" if m == 1 else _apocope(numero_a_palabras(m)) + " mil"
        return pre + ("" if r == 0 else " " + numero_a_palabras(r))
    if n < 1_000_000_000_000:
        m, r = divmod(n, 1_000_000)
        pre = "un millón" if m == 1 else _apocope(numero_a_palabras(m)) + " millones"
        return pre + ("" if r == 0 else " " + numero_a_palabras(r))
    m, r = divmod(n, 1_000_000_000_000)
    pre = "un billón" if m == 1 else _apocope(numero_a_palabras(m)) + " billones"
    return pre + ("" if r == 0 else " " + numero_a_palabras(r))


def _apocope(texto: str) -> str:
    """'veintiuno mil' -> 'veintiún mil'; 'uno' -> 'un'."""
    if texto.endswith("veintiuno"):
        return texto[:-9] + "veintiún"
    if texto.endswith("uno"):
        return texto[:-3] + "un"
    return texto


def _numeros(texto: str) -> str:
    def decimal(m: re.Match) -> str:
        ent, dec = m.group(1).replace(".", ""), m.group(3)
        return f" {numero_a_palabras(int(ent))} coma {' '.join(numero_a_palabras(int(c)) for c in dec) if dec.startswith('0') else numero_a_palabras(int(dec))} "

    # 1.234.567 (miles con punto) -> 1234567
    texto = re.sub(r"\b\d{1,3}(?:\.\d{3})+\b(?![.,]\d)", lambda m: m.group(0).replace(".", ""), texto)
    texto = re.sub(r"\b(\d+)([.,])(\d+)\b", decimal, texto)
    texto = re.sub(r"\d+", lambda m: " " + numero_a_palabras(int(m.group(0))) + " "
                   if len(m.group(0)) <= 15 else " " + " ".join(UNIDADES[int(c)] for c in m.group(0)) + " ", texto)
    return texto


def normalizar(texto: str, lexico: dict[str, str] | None = None) -> str:
    """Prepara el texto: léxico propio, símbolos, números y siglas."""
    texto = unicodedata.normalize("NFC", texto)
    texto = texto.replace("\n", " ").replace("’", "'")
    if lexico:
        for palabra, dicha in lexico.items():
            texto = re.sub(rf"(?<!\w){re.escape(palabra)}(?!\w)", dicha, texto, flags=re.IGNORECASE)
    for s, d in SIMBOLOS.items():
        texto = texto.replace(s, d)
    texto = _numeros(texto)

    # Siglas en mayúsculas sin vocales suficientes se deletrean (p. ej. "PDF").
    def sigla(m: re.Match) -> str:
        w = m.group(0)
        if len(w) <= 5 and not re.search(r"[AEIOU][^AEIOU]?[AEIOU]|[AEIOU]$", w) or len(w) <= 2:
            return " ".join(LETRAS.get(c.lower(), c) for c in w)
        return w

    texto = re.sub(r"\b[A-ZÑ]{2,}\b", sigla, texto)
    texto = re.sub(r"[¿¡«»\"“”()\[\]{}*_/\\|<>~^]", " ", texto)
    texto = re.sub(r"\s*[-–]\s*", " ", texto)
    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()


def _unidades(palabra: str) -> list[tuple[str, str]]:
    """Convierte letras en unidades (fonema, clase). Clase: 'v' vocal, 'c' consonante."""
    w = palabra
    out: list[tuple[str, str]] = []
    i = 0
    n = len(w)

    def sig(k: int = 1) -> str:
        return w[i + k] if i + k < n else ""

    while i < n:
        c = w[i]
        if c in VOCALES:
            if c == "u" and i > 0 and w[i - 1] in "qg" and sig() in "eiéí" and sig() != "":
                i += 1  # u muda en que, qui, gue, gui
                continue
            out.append((c, "v"))
        elif c == "y":
            # 'y' es vocal al final de palabra tras vocal (hoy, muy) o sola
            if (i == n - 1 and i > 0) or n == 1:
                out.append(("i", "v"))
            elif sig() in VOCALES:
                out.append(("ʝ", "c"))
            else:
                out.append(("i", "v"))
        elif c == "c":
            if sig() == "h":
                out.append(("ʧ", "c"))
                i += 1
            elif sig() in "eiéí" and sig() != "":
                out.append(("s", "c"))
            else:
                out.append(("k", "c"))
        elif c == "q":
            out.append(("k", "c"))
        elif c == "g":
            out.append(("x", "c") if sig() in "eiéí" and sig() != "" else ("g", "c"))
        elif c == "j":
            out.append(("x", "c"))
        elif c == "h":
            pass  # muda
        elif c == "l":
            if sig() == "l":
                out.append(("ʝ", "c"))
                i += 1
            else:
                out.append(("l", "c"))
        elif c == "r":
            if sig() == "r":
                out.append(("r", "c"))
                i += 1
            elif i == 0 or w[i - 1] in "lns":
                out.append(("r", "c"))
            else:
                out.append(("ɾ", "c"))
        elif c == "ñ":
            out.append(("ɲ", "c"))
        elif c in "vb":
            out.append(("b", "c"))
        elif c == "z":
            out.append(("s", "c"))
        elif c == "x":
            if i == 0:
                out.append(("s", "c"))
            else:
                out.append(("k", "c"))
                out.append(("s", "c"))
        elif c == "w":
            out.append(("w", "c") if sig() in VOCALES and sig() != "" else ("u", "v"))
        elif c == "k":
            out.append(("k", "c"))
        elif c.isalpha():
            out.append((c, "c"))
        i += 1
    return out


def _nucleos(unidades: list[tuple[str, str]]) -> list[list[int]]:
    """Agrupa vocales seguidas en núcleos silábicos (diptongos e hiatos)."""
    nucleos: list[list[int]] = []
    i = 0
    while i < len(unidades):
        if unidades[i][1] != "v":
            i += 1
            continue
        j = i
        while j < len(unidades) and unidades[j][1] == "v":
            j += 1
        grupo = list(range(i, j))
        actual: list[int] = []
        for k in grupo:
            v = unidades[k][0]
            fuerte = v in FUERTES or v in "íú"
            if not actual:
                actual = [k]
                continue
            prev_fuertes = [x for x in actual if unidades[x][0] in FUERTES or unidades[x][0] in "íú"]
            if fuerte and prev_fuertes:
                nucleos.append(actual)  # hiato
                actual = [k]
            else:
                actual.append(k)
        nucleos.append(actual)
        i = j
    return nucleos


def palabra_a_fonemas(palabra: str) -> str:
    palabra = palabra.lower()
    unidades = _unidades(palabra)
    if not unidades:
        return ""
    nucleos = _nucleos(unidades)
    tonico = None
    if palabra not in ATONAS:
        for idx, nuc in enumerate(nucleos):
            if any(unidades[k][0] in "áéíóú" for k in nuc):
                tonico = idx
        if tonico is None and nucleos:
            ultima = palabra[-1]
            if len(nucleos) == 1:
                tonico = 0
            elif ultima in "aeiouns":
                tonico = len(nucleos) - 2
            else:
                tonico = len(nucleos) - 1
    # Fonema de cada vocal: núcleo o semivocal (j, w)
    fonema = [u[0] for u in unidades]
    marca_antes: set[int] = set()
    for idx, nuc in enumerate(nucleos):
        if len(nuc) == 1:
            pico = nuc[0]
        else:
            fuertes = [k for k in nuc if unidades[k][0] in FUERTES or unidades[k][0] in "íú"]
            pico = fuertes[0] if fuertes else nuc[-1]
        for k in nuc:
            base = TILDES.get(unidades[k][0], unidades[k][0])
            if k == pico:
                fonema[k] = base
            elif k < pico:
                fonema[k] = "j" if base == "i" else "w" if base == "u" else base
            else:  # diptongo decreciente, como espeak-ng: oɪ, eɪ, aʊ
                fonema[k] = "ɪ" if base == "i" else "ʊ" if base == "u" else base
        if idx == tonico:
            marca_antes.add(pico)
    # Alófonos dentro de la palabra
    res: list[str] = []
    for k, f in enumerate(fonema):
        prev = fonema[k - 1] if k > 0 else ""
        nxt = fonema[k + 1] if k + 1 < len(fonema) else ""
        if f in "bdg" and k > 0 and prev not in ("m", "n", "") and not (f == "d" and prev == "l"):
            f = {"b": "β", "d": "ð", "g": "ɣ"}[f]
        elif f == "n" and nxt in ("b", "p", "m"):
            f = "m"
        elif f == "n" and nxt in ("k", "g", "x"):
            f = "ŋ"
        if f == "g":
            f = "ɡ"  # el vocabulario de Kokoro usa U+0261, no la g latina
        if k in marca_antes:
            res.append("ˈ")
        res.append(f)
    return "".join(res)


_SUAVE = {"b": "β", "d": "ð", "g": "ɣ", "ɡ": "ɣ"}


def _enlazar(previa: str, actual: str) -> str:
    """b, d, g al inicio de palabra se suavizan si la palabra previa no acaba en pausa o nasal."""
    if not previa or not actual or previa[-1] in ".,!?;:…mnŋ":
        return actual
    ini = actual[1] if actual[0] == "ˈ" and len(actual) > 1 else actual[0]
    if ini not in _SUAVE or (ini == "d" and previa[-1] == "l"):
        return actual
    if actual[0] == "ˈ":
        return "ˈ" + _SUAVE[ini] + actual[2:]
    return _SUAVE[ini] + actual[1:]


_TOKEN = re.compile(r"[a-záéíóúüñ]+|[.,!?;:…]", re.IGNORECASE)


def texto_a_fonemas(texto: str, lexico: dict[str, str] | None = None) -> str:
    """Texto español -> cadena de fonemas para Kokoro."""
    texto = normalizar(texto, lexico)
    partes: list[str] = []
    for tok in _TOKEN.findall(texto):
        if tok in ".,!?;:…":
            if partes:
                partes[-1] = partes[-1] + tok
            continue
        f = palabra_a_fonemas(tok)
        if f:
            partes.append(_enlazar(partes[-1] if partes else "", f))
    return " ".join(partes)


def dividir_frases(texto: str, max_car: int = 220) -> list[str]:
    """Parte el texto en frases para generar y enviar audio frase a frase."""
    texto = texto.strip()
    if not texto:
        return []
    trozos = re.split(r"(?<=[.!?…;:])\s+|\n+", texto)
    frases: list[str] = []
    for t in trozos:
        t = t.strip()
        while len(t) > max_car:
            corte = t.rfind(",", 0, max_car)
            if corte < 40:
                corte = t.rfind(" ", 0, max_car)
            if corte < 1:
                corte = max_car
            frases.append(t[: corte + 1].strip())
            t = t[corte + 1:].strip()
        if t:
            frases.append(t)
    return frases
