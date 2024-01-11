# Fibonacci sequence

In mathematics, the **Fibonacci sequence** is a sequence in which each number is the sum of the two preceding ones. Numbers that are part of the Fibonacci sequence are known as Fibonacci numbers.

> 0, 1, 1, 2, 3, 5, 8, 13, . . .

## Problem:

Write a generator that takes a range from user and prints the fibonacci sequence up to that range.


## Solution:

To solve this problem we need to work with generators.

- A Generator is a function that returns an iterator using the Yield keyword.
- The output of the generator function is a generator object.
- In order to see the result of generator we need to pass the generator to next() method. or use a for loop.

```bash
def fibogen(n):
    a = 0
    b = 1

    while n > 0:
        yield a
        a, b = b, a + b     # Multiple assignment of variables.
        n -= 1      # To make sure the while lopp would stop iterating when done.
```

In this solution a and b are used as place holders for the first two numbers in the fibonacci sequence. then when the range is enterd the while loop starts iterating and first a is yielded and `a, b = b, a + b`. a is equal to b and b is equal to a + b and n is incremenated by 1 to make sure the loop stops at one point. in the next iteration this time, `yield a` is the result of the last two numbers (a + b) and it keeps going on and on within range.

> yield is the keyword for generator functions. and it returns a generator object.

Now that calculation is done we can print the result by using for loops or `list()` method.

**For loop:**

```bash
n = int(input("Enter the range to calculate: "))

generator_object = fibogen(n)
for i in generator_object:
    print(i)
```

**list() method:**
 
```bash
n = int(input("Enter the range to calculate: "))
print(list(fibogen(n)))
```

**Since this problem has many solutions, 3 are included in the problem directory. Feel free to take a look if you'd like.**

link to solution files:
- [Fibonacci sequence generator solution](fibonacci_generator.py)
- [Fibonacci sequence generator with caching solution](fibonacci_generator_cache.py)
- [Fibonacci sequence recursive with caching solution](fibonacci_recursive.py)


## Tests:

Tests are performed with diffrent inputs.

link to test file:
[Fibonacci sequence generator test](test_fionacci.py)

- in order to run tests pls make sure that **pytest** is installed on your environment. Then use `pytest -v` command to run tests in verbose mode.