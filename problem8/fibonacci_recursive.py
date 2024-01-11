# Using Recursive function with functools.cache for big ranges and avoid recursive errors
from functools import cache


@cache
def fibo(n):
   
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
 


if __name__ == "__main__":
    n = int(input("Enter the range to calculate: "))

    # Print result using for loop
    for i in range(0, n):
        print(fibo(i))


    # Print result using list comprehension
    # print([fibo(i) for i in range(0,n)])