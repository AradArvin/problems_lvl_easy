

def is_an_expo_of_2(n):

    for i in range(n):
        m = 2 ** i

        if m == n:
            return True
        
    return False



if __name__ == "__main__":
    while True:
        try:
            n = int(input("Please Enter a number: "))
            if is_an_expo_of_2(n) == True:
                print(str(n) + " is a power of 2")
            else:
                print(str(n) + " is not a power of 2")
            break   
        except ValueError:
            print(">>>Entered value must be a number, pls try again!\n")