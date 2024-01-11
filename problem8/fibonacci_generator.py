# Using generators


def fibogen(n):
    a = 0
    b = 1

    while n > 0:
        yield a
        a, b = b, a + b     # Multiple assignment of variables.
        n -= 1      # To make sure the while lopp would stop iterating when done.



if __name__ == "__main__":
    n = int(input("Enter the range to calculate: "))

    generator_object = fibogen(n)
    for i in generator_object:
        print(i)