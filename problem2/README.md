# Exponentiation of 2

A number is an expo of 2 if a power of 2 is equal to the number.

- 2 ** 0 = 1
- 2 ** 1 = 2
- 2 ** 2 = 4
- 2 ** 3 = 8
- 2 ** 4 = 16
- 2 ** 5 = 32
- ...

## Problem:

Take an input from user and see if the number is an expo of 2. and return an string telling if the number is an expo of 2 or not >


**Examples:**

- (2 ** n) != 7
- 7 is not an expo of 2

- (2 ** 3) == 8
- 8 is an expo of 2


## Solution:

In this problem we simply need to work with exponentiation `**` arithmetic operator.

```bash
def is_an_expo_of_2(n):

    for i in range(n):
        m = 2 ** i

        if m == n:
            return True
        
    return False
```

This function simply checkes if the entered number is an expo of 2, then returns True or False.

Once we have the result of function, then we can use an if condition to `stdout(print)` the string answer >

```bash
if is_an_expo_of_2(n) == True:
    print(str(n) + " is a power of 2")
else:
    print(str(n) + " is not a power of 2")
```

link to solution file:
[Exponentiation solution](expo_of_2.py)


## Tests:

Tests are performed with diffrent inputs.

link to test file:
[Exponentiation test](test_expo_of_2.py)

- in order to run tests pls make sure that **pytest** is installed on your environment. Then use `pytest -v` command to run tests in verbose mode.