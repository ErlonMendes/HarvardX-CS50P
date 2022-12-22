from numb3rs import validate


def test_format():
    assert validate("0.0.0.0") is True
    assert validate("0.0.0") is False
    assert validate("0.0") is False
    assert validate("0") is False


def test_range():
    assert validate("255.255.255.255") is True
    assert validate("256.255.255.255") is False
    assert validate("255.256.255.255") is False
    assert validate("255.255.256.255") is False
    assert validate("255.255.255.256") is False


def test_others():
    assert validate("140.247.235.144") is True


def test_cat():
    assert validate("cat") is False


# Executar pytest test_numb3rs.py no Terminal
