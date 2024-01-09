from count_chars_in_string import counter


def test_count_of_chars_in_str():
    string = "www.yahoo.com"
    assert counter(string) == {'w': 3, '.': 2, 'y': 1, 'a': 1, 'h': 1, 'o': 3, 'c': 1, 'm': 1}, "Wrong input!"


def test_count_in_empty_string():
    string = ""
    assert counter(string) == {}, "Not empty!"