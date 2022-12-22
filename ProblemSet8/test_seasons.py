from seasons import check_birthday
import pytest


def test_pass():
    assert check_birthday("1978-04-29") == ("1978", "04", "29")


def test_not_pass():
    with pytest.raises(ValueError):
        check_birthday("29-04-1978")

# Executar pytest test_seasons.py no Terminal
