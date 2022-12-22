from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(5)
    assert jar.capacity == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(3)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(6)
    assert jar.size == 6
    jar.withdraw(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(4)

# Executar pytest test_jar.py no Terminal
