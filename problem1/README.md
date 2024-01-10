# The perfect number

A number is perfect when the sum of it's remainders is equal to itself.
> (1+2+3) = 6


## Problem:

Take an input from user and see if the sum of remainders of the input number is equal to the entered number. If equal then return `Yes`, else return `No`.


**Examples:**

1. (1+3+9) != 27 
    - 27 is not a perfect number therefor the answer is `No`

2. (1+2+3) == 6
    - 6 is a perfect number therefor the answer is `Yes`


## Solution:

As it was pointed out earlier we must work with the remainder to solve this problem >

```bash
def is_perfect(n):
    sum_of_remainders = 0

    for i in range(1, n):
        if n % i == 0:
            sum_of_remainders += i

    return sum_of_remainders
```

This function first takes the number as input and then puts the `n` inside a loop wher the loop iterates over the range of `n` and when the remainder of the number in range is equal to 0 then that remainder is added to `sum_of_remainders`. Therefor in the end when the loop is exhausted, function returns the total of `sum_of_remainders`. In the end if `sum_of_remainders` == `n`, then the number is perfect.

Once the output is out then we only need to use an if condition to check the output >
```bash
if is_perfect(n) == n:
    print("Yes")
else:
    print("No")
```

link to solution file:
[Perfect number solution](perfect_number.py)


## Tests:

Tests are performed with diffrent inputs.

link to test file:
[Perfect number test](test_perfect_number.py)

- in order to run tests pls make sure that **pytest** is installed on your environment. Then use `pytest -v` command to run tests in verbose mode.