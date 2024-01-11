# Using generators with custom caching for big ranges


def fib(num):
    a = 0
    b = 1

    for i in range(num):
        yield a
        temp = a    # Making a temproray variable to save the last result and therfor basic caching the result.
        a = b
        b = temp + b



if __name__ == "__main__":
    n = int(input("Enter the range to calculate: "))
    
    for i in fib(n):
        print(i)