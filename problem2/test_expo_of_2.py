from expo_of_2 import is_an_expo_of_2


def test_if_number_is_equal_to_an_expo_of_2():
    """
    2 ** 3 == 8
    """
    n = 8
    assert is_an_expo_of_2(n) == True, "Supposed to be True"


def test_if_number_is_not_equal_to_an_expo_of_2():
    """
    (2 ** n) != 7
    """
    n = 7
    assert is_an_expo_of_2(n) == False, "Supposed to be False"