from bank import value


def test_hello():
    assert value("Hello") == 0


def test_h():
    assert value("Hey") == 20


def test_none():
    assert value("Oi") == 100

# Executar pytest test_bank.py no Terminal
