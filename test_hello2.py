from hello5 import hello


def test_default():
    assert hello() == "Hello, world"


def test_arguments():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"Hello, {name}"

# Executar pytest test_hello2.py no Terminal
