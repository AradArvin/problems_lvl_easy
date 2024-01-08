from white_space import cap_space


def test_func_should_not_leave_white_spaces_at_the_start_and_end_of_string():
    string = " The "
    spaced = cap_space(string)
    assert spaced == "The", "Whitespaces at the end or start of string exist!"


def test_func_should_insert_white_spaces_before_capital_letters():
    string = "TheFirstLetter"
    spaced = cap_space(string)
    assert spaced == "The First Letter", "Whitespaces where not inserted!"