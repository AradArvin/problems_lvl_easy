


def sorting_the_list(list_of_tuples):
    sorted_list = sorted(list_of_tuples, key=lambda x: x[-1])
    return sorted_list



if __name__ == "__main__":
    input_list = [(3, 8), (10, 25), (5, 4), (12, 7), (15, 9)]
    print(sorting_the_list(input_list))