from fuel import convert, gauge
import pytest


def test1():
    assert convert("3/4") == 75 and gauge(75) == "75%"


def test2():
    assert convert("1/100") == 1 and gauge(1) == "E"


def test3():
    assert convert("99/100") == 99 and gauge(99) == "F"


def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")

# Executar pytest test_fuel.py no Terminal
