from perfect_number import is_perfect


def test_number_is_not_perfect():
    """
    (1+3+9) != 27
    """
    n = 27
    assert is_perfect(n) == 13, "The number is supposed to be not perfect!"


def test_number_is_perfect():
    """
    (1+2+3) == 6
    """
    n = 6
    assert is_perfect(n) == 6, "The number is supposed to be perfect!"