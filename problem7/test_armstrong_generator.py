# For generator version
from armstrong_generator import check_armstrong


def test_is_an_armstrong_number():
    number = "153"
    generator = check_armstrong(number)
    assert next(generator) == 153, "Not an armstrong number!" 


def test_is_not_an_armstrong_number():
    number = "200"
    generator = check_armstrong(number)
    assert next(generator) != 200, "could be an armstrong number" 