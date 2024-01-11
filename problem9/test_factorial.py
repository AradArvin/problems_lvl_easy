from factorial_func import factorial_func


def test_function_works():
    num = 5
    assert factorial_func(num) == 120, "Wrong output!"