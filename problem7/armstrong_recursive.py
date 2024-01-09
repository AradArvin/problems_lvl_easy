# Using recursive function

def check_armstrong(number, temp, sum, expo= None):
    expo = len(str(number))

    if temp == 0:
        if sum == number:
            return True
        else:
            return False
        
    digit = temp % 10
    sum += digit ** expo
    temp = temp // 10

    return check_armstrong(number, temp, sum, expo)



if __name__ == "__main__":
    number = int(input("Please Enter a Number: "))
    temp = number
    sum = 0
    result = check_armstrong(number, temp, sum)

    if result:
        print(number,"is an Armstrong number")
    else:
        print(number,"is not an Armstrong number")