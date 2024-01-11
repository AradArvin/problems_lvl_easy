# A very basic approach

def multiply_table():
    number = 1

    for j in range(1,10+1):
        print()
        for i in range(1,10+1):
            print(number * i * j, end="\t")


if __name__ == "__main__":
    multiply_table()