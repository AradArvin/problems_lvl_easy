


def sum_of_items(string):
    sum_letter = 0
    sum_digit = 0

    for i in string:
        if i.isalpha():
            sum_letter += 1
        elif i.isdigit():
            sum_digit += 1

    return sum_digit, sum_letter



if __name__ == "__main__":
    string = input("Please Enter a string containing letters and numbers: ")
    digit_sum, letter_sum = sum_of_items(string)

    print("Digits: " + str(digit_sum))
    print("Letters: " + str(letter_sum))