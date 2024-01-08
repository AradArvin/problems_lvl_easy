

def is_perfect(n):
    sum_of_remainders = 0

    for i in range(1, n):
        if n % i == 0:
            sum_of_remainders += i

    return sum_of_remainders



if __name__ == "__main__":
    while True:
        try:
            n = int(input("Please Enter a Number: "))
            if is_perfect(n) == n:
                print("Yes")
            else:
                print("No")
            break
        except ValueError:
            print(">>>Entered value must be a number, pls try again!\n")