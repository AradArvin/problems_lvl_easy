# Using generators

def check_armstrong(number):
   expo = len(number)
   list_number = list(map(int, number))
   result = sum(list(map(lambda x: x ** expo, list_number)))
   yield result



if __name__ == "__main__":
    try:
        number = input("Please Enter a Number: ")
        generator = check_armstrong(number)
        result = next(generator)

        if result == int(number):
            print(number, "is an Armstrong number")
        else:
            print(number, "is not an Armstrong number")

    except ValueError:
        print("<<Input must be a positive number!>>")
    
    