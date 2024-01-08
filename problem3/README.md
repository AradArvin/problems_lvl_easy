# Count letters & digits in a string

There are diffrent ways to count characters in a string. how ever the best way is to use built in methods to write a clean and meaningful code.


## Problem:

Take an input string from user and return the amount of letters and digits in the string to the user.


**Examples:**

String = "Python 3.12.1"
Digits = 4
Letters = 6

String = "through 8707 program"
Digits = 4
Letters = 14


## Solution:

This problem is easily solveable with built in methods: isalpha(), isdigit()
- isdigit() > checks to see if a character in string is a digit
- isalpha() > checks to see if a character in string is a alphabet letter

```bash
def sum_of_items(string):
    sum_letter = 0
    sum_digit = 0

    for i in string:
        if i.isalpha():
            sum_letter += 1
        elif i.isdigit():
            sum_digit += 1

    return sum_digit, sum_letter
```

As you can see a condition is used to check the type of letter. If the condition is met character is added to the sum variable defined before the loop. in the end the function returns sum of digits and sum of letters as result.

> keep in mind that this function can be broken into 2 functions. one for letters and one for digits.

Once the result is returnd then we only need to print the result to user in `stdout` or standard output >

```bash
digit_sum, letter_sum = sum_of_items(string)
print("Digits: " + str(digit_sum))
print("Letters: " + str(letter_sum))
```

link to solution file:
[Count characters solution](count_in_str.py)


## Tests:

Tests are performed with diffrent inputs.

link to test file:
[Count characters test](test_count_in_str.py)

- in order to run tests pls make sure that **pytest** is installed on your environment. Then use `pytest -v` command to run tests in verbose mode.