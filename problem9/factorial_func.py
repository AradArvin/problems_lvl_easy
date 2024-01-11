# Naive method without built-in methods


def factorial_func(num):
    result = 1

    for i in range(1, num + 1):     # Last number is not included in range so we increase it by 1.
        result *= i     # Equal to (result = result * i )

    return result


if __name__ == "__main__":
	num = int(input("Enter a number: "))
	
	print(f"The factorial of {num} is : {factorial_func(num)}")     # f is used to format a string