from sorting import sorting_the_list


def test_sorting_a_list_of_tuples():
    input_list = [(1, 4), (3, 1), (4, 2)]
    assert sorting_the_list(input_list) == [(3, 1), (4, 2), (1, 4)], "Sorting failed!"