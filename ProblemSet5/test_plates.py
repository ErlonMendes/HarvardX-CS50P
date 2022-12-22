from plates import is_valid


def test1():
    assert is_valid("CS50") is True


def test2():
    assert is_valid("50") is False


def test3():
    assert is_valid("CS05") is False


def test4():
    assert is_valid("CS50P") is False


def test5():
    assert is_valid("PI3.14") is False


def test6():
    assert is_valid("H") is False


def test7():
    assert is_valid("OUTATIME") is False

# Executar pytest test_plates.py no Terminal
