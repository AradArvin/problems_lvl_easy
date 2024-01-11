# Multiplication table

Multiplication table is a table that shows the product of numbers 1 throught 10.

- 1       2       3       4       5       6       7       8       9       10
- 2       4       6       8       10      12      14      16      18      20
- 3       6       9       12      15      18      21      24      27      30
- 4       8       12      16      20      24      28      32      36      40
- 5       10      15      20      25      30      35      40      45      50
- 6       12      18      24      30      36      42      48      54      60
- 7       14      21      28      35      42      49      56      63      70
- 8       16      24      32      40      48      56      64      72      80
- 9       18      27      36      45      54      63      72      81      90
- 10      20      30      40      50      60      70      80      90      100 


## Problem:

Write a function to print the multiplication table as shown above.


## Solution:

This problem can be solved using nested for loops.

```bash
def multiply_table():
    number = 1

    for j in range(1,10+1):
        print()
        for i in range(1,10+1):
            print(number * i * j, end="\t")
```

As we can see we are using ranges with nested for loops to print the multiplication table. we use `number = 1` to indicate that all the numbers are multiplies of 1. and `end="\t"` means end each print with a tab, there is a tab of space between each number in line.

Then we simply need to call this function to see the result in stdout.

link to solution files:
[Multiplication table solution](mul_table.py)

> This can be solved in many ways. try them your self. a best practice would be to use diffrent data sequences for this problem.