# Armstrong number

A number is armstrong when the sum of each digit to the exponentiation of the len of number is equal to the original number.

- 153 is an armstrong number -> 1 ** 3 + 5 ** 3 + 3 ** 3 == 153
- 1634 is an armstrong number -> 1 ** 4 + 6 ** 4 + 3 ** 4 + 4 ** 4 == 1634

- 200 is not an armstrong number -> 2 ** 3 + 0 ** 3 + 0 ** 3 != 200
- 1562 is not an armstrong number -> 1 ** 4 + 5 ** 4 + 6 ** 4 + 2 ** 4 != 1562


## Problem:

Write a generator that checks if a number is armstrong then print the result in stdout >


**Examples:**

1. input = 153
    - output = 153 is an armstrong number

2. input = 200
    - output = 200 is not an armstrong number


## Solution:

To solve this problem we need to work with generators.

- A Generator is a function that returns an iterator using the Yield keyword.
- The output of the generator function is a generator object.
- In order to see the result of generator we need to pass the generator to next() method.

```bash
def check_armstrong(number):
   expo = len(number)
   list_number = list(map(int, number))
   result = sum(list(map(lambda x: x ** expo, list_number)))
   yield result
```

The generator first takes the number as argument. (***keep in mind that the type of input() method is always str***). then the exponentiation is callculated to be the len of number. next we turn the number into a list of integers by braking the number to it's digits. here `map()` method is used to take each character of the string and turn their type to int and then `list()` is used to turn the number string into a list of it's digits. in the next line we use map again to increase each digit in the list to the power named expo. cased inside a `list()` to keep the result of `map()` as a list. and finally cased in `sum()` to get the sum of numbers in the result list. and in the end `yield` keyword is used to return a generator object.

> len() -> gets the len of data sequence.

> list() -> creates a list.

> map() -> executes a specified function for each item in an iterable. The item is sent to the function as a parameter.


**lambda:** _A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression._

**lambda syntax:** _lambda arguments : expression_


Now that we have the generator object we can give it to **next()** method to see the result and check our conditions >

```bash
number = input("Please Enter a Number: ")
generator = check_armstrong(number)
result = next(generator)

if result == int(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
```

> **int()** is used to change the type of number from str to int.

**Please keep in mind that each problem can be solved in many ways. with that being said the recursive function approach is included in the problem directory as well.**

link to solution file:
[Armstrong number generator solution](armstrong_generator.py)
[Armstrong number recursive solution](armstrong_recursive.py)


## Tests:

Tests are performed with diffrent inputs.

link to test file:
[Armstrong number generator test](test_armstrong_generator.py)

- in order to run tests pls make sure that **pytest** is installed on your environment. Then use `pytest -v` command to run tests in verbose mode.