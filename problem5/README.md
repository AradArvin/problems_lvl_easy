# Sorting tuples inside a list

Sorting in data sets is sometimes an important operation. So we have this problem with is about sorting in a list.


## Problem:

We have a list of tuples and we want to sort this list by the last element of tuples in increasing order.


**Examples:**

1. list_of_tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    - expcted_output = [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

2. list_of_tuples = [(3, 8), (10, 25), (5, 4), (12, 7), (15, 9)]
    - expcted_output = [(5, 4), (12, 7), (3, 8), (15, 9), (10, 25)]


## Solution:

The solution to this problem is fairly easy all you need to do is to use sorted() built-in method and a lambda function as a key to be sorted with.

syntax: sorted(data_sequence, key)

> Here in this problem data_sequence is a list of tuples and key is the last element of tuples.

lambda: is a one line temprory function that is used to shorten code and to avoid writing functions that wont be used in diffrent places of program.(single use function)

```bash
def sorting_the_list(list_of_tuples):
    sorted_list = sorted(list_of_tuples, key=lambda x: x[-1])
    return sorted_list
```

This function first takes a list of tuples as an argument and then uses sorted method with the last element key `key=lambda x: x[-1]` to perform sorting on the input list and then simply returns the output.

In the end we can simply use print on the function call to print the output to stdout.

```bash
input_list = [(3, 8), (10, 25), (5, 4), (12, 7), (15, 9)]
print(sorting_the_list(input_list))
```

link to solution file:
[List sorting solution](sorting.py)


## Tests:

Tests are performed with diffrent inputs.

link to test file:
[List sorting test](test_sorting.py)

- in order to run tests pls make sure that **pytest** is installed on your environment. Then use `pytest -v` command to run tests in verbose mode.