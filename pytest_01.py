import math


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5


def test_square():
    # num = 7
    assert 7 * 7 == 49


def test_equality():
    assert 10 == 10


# pytest pytest_01.py -v --junitxml=result.xml
if __name__ == '__main__':
    test_sqrt()
    test_square()
    test_equality()
