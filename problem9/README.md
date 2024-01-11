# Factorial of a number

Factorial of a number is the product of all positive integers lesss than or equal to that number.

> 5! = 120 -> 1 * 2 * 3 * 4 * 5


## Problem:

Write a program to calculate the factorial of a number.

**Examples:**

1. input = 5
    - output = 120

2. input = 10
    - output = 3628800


## Solution:

Solving this problem is fairly easy >

```bash
def factorial_func(num):
    result = 1

    for i in range(1, num + 1):     # Last number is not included in range so we increase it by 1.
        result *= i     # Equal to (result = result * i )

    return result
```

This function multiplies all th numbers in range the number entered by the user and then returnes the result.

To print the result we simply use `print()` method >

```bash
num = int(input("Enter a number: "))
print(f"The factorial of {num} is : {factorial_func(num)}")     # f is used to format a string
```

link to solution files:
- [Factorial naive solution](factorial_func.py)
- [Factorial built-in methods solution](factorial_builtin_methods.py)
- [Factorial recursive solution](factorial_recursive.py)

> Please keep in mind that there is a built in factorial method in the math library. (math.factorial())


## Tests:

Tests are performed with diffrent inputs.

link to test file:
[Factorial naive test](test_factorial.py)

- in order to run tests pls make sure that **pytest** is installed on your environment. Then use `pytest -v` command to run tests in verbose mode.