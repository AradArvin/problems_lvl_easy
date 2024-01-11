# Tests for fibonacci generator 
from typing import Generator
from fibonacci_generator import fibogen


def test_generator_obj_creation():
    n = 0
    assert isinstance(fibogen(n), Generator), "Not a generator!"


def test_fibonacci_generator_works_fine():
    n = 5
    assert list(fibogen(n)) ==  [0, 1, 1, 2, 3]