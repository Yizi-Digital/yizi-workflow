import json
from pathlib import Path

from app.g2p_es import dividir_frases, normalizar, numero_a_palabras, palabra_a_fonemas, texto_a_fonemas

VOCAB = json.loads((Path(__file__).resolve().parent.parent / "app/kokoro_vocab.json").read_text(encoding="utf-8"))


def test_numeros():
    assert numero_a_palabras(0) == "cero"
    assert numero_a_palabras(21) == "veintiuno"
    assert numero_a_palabras(100) == "cien"
    assert numero_a_palabras(1999) == "mil novecientos noventa y nueve"
    assert numero_a_palabras(21000) == "veintiún mil"
    assert numero_a_palabras(2_000_000) == "dos millones"
    assert "por ciento" in normalizar("el 30%")


def test_acento_y_alofonos():
    assert palabra_a_fonemas("hola") == "ˈola"
    assert palabra_a_fonemas("canción") == "kansjˈon"
    assert palabra_a_fonemas("ciudad") == "sjuðˈað"
    assert palabra_a_fonemas("guerra") == "ɡˈera"
    assert palabra_a_fonemas("hoy") == "ˈoɪ"
    assert palabra_a_fonemas("de") == "de"  # átona


def test_enlace_entre_palabras():
    assert texto_a_fonemas("buenos días") == "bwˈenos ðˈias"


def test_todo_en_vocabulario():
    f = texto_a_fonemas("¿Cuánto cuesta el pedido? Son 25 dólares, ¡gracias! Año, guitarra, pingüino, examen, chocolate.")
    fuera = {c for c in f if c not in VOCAB}
    assert not fuera, fuera


def test_dividir_frases():
    assert dividir_frases("Hola. ¿Qué tal? Bien!") == ["Hola.", "¿Qué tal?", "Bien!"]
    largas = dividir_frases("palabra " * 100)
    assert all(len(x) <= 221 for x in largas)
