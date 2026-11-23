import pytest

from app import ajustes


def test_por_defecto_es_local(monkeypatch):
    monkeypatch.delenv("YIZI_VOZ_TOKEN", raising=False)
    a = ajustes.cargar()
    assert a.host == "127.0.0.1"
    assert a.puerto == 8765
    assert a.token == ""
    assert "vision" in a.agentes and "edith" in a.agentes


def test_rechaza_todas_las_interfaces(tmp_path):
    c = tmp_path / "c.yaml"
    c.write_text("servidor:\n  host: 0.0.0.0\n", encoding="utf-8")
    with pytest.raises(ValueError):
        ajustes.cargar(c)


def test_token_solo_por_entorno(monkeypatch):
    monkeypatch.setenv("YIZI_VOZ_TOKEN", "x1")
    assert ajustes.cargar().token == "x1"
