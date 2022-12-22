from twttr import shorten


def test_lower():
    assert shorten("Testando") == "Tstnd"


def test_upper():
    assert shorten("tEstAndO") == "tstnd"


def test_number():
    assert shorten("Teste1") == "Tst1"


def test_punctuation():
    assert shorten("Teste.") == "Tst."

# Executar pytest test_twttr.py no Terminal
