from hello4 import hello


def test_hello():
    assert hello("David") == "Hello, David"

# O teste não irá funcionar porque a função hello não está retornando um valor, está apenas printando a frase
