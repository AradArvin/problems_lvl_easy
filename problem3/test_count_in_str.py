from count_in_str import sum_of_items



def test_if_there_are_letters_in_string():
    string = "python"
    digit_sum, letter_sum = sum_of_items(string)

    assert letter_sum != 0, "No letters in the string!"


def test_if_there_are_digits_in_string():
    string = "3.12.1"
    digit_sum, letter_sum = sum_of_items(string)

    assert digit_sum != 0, "No digits in the string!"


def test_count_letters_and_digits():
    string = "Python 3.12.1"
    digit_sum, letter_sum = sum_of_items(string)

    assert letter_sum == 6, "The number of letters shuold be 6"
    assert digit_sum == 4, "The number of digits should be 4"