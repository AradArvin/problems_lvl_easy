# Counting the number of characters in string using dictionary

To count the number of characters in a string we can simply use dictionaries where the key is the character and value is its rarity number.

dictionary = {key: value, ...}

## Problem:

Write a program which can count the number of each character in the string.


**Examples:**

1. input_string = "www.github.com"
    - output = {'w': 3, '.': 2, 'g': 1, 'i': 1, 't': 1, 'h': 1, 'u': 1, 'b': 1, 'c': 1, 'o': 1, 'm': 1}

2. input_string = "internationalization"
    - output = {'i': 4, 'n': 4, 't': 3, 'e': 1, 'r': 1, 'a': 3, 'o': 2, 'l': 1, 'z': 1}


## Solution:

To solve this problem as it was said earlier we use dictionary data sequence >

```bash
def counter(string):
    count = {}

    for s in string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    return count
```

We first create an empty dictionary named count and then if we have a key in the dictionary we increase the number in its' value by one or if the key does not exist we create it and set it's value equal to 1.


Then we print the output.

```bash
string = input("Please Enter text: \n")
print(counter(string))
```

link to solution file:
[character counting solution](count_chars_in_string.py)


## Tests:

Tests are performed with diffrent inputs.

link to test file:
[character counting test](test_count_chars_in_string.py)

- in order to run tests pls make sure that **pytest** is installed on your environment. Then use `pytest -v` command to run tests in verbose mode.