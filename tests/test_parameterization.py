import pytest


def add(a, b):
    return a + b


@pytest.mark.parametrize("a,b,expected",
    [(10, 5, 15),
     (-1, 1, 0),
     (-1, -1, -2)])
def test_add(a, b, expected):
    assert add(a, b) == expected
