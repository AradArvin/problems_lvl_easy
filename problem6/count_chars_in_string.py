

def counter(string):
    count = {}

    for s in string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    return count



if __name__ == "__main__":
    string = input("Please Enter text: \n")
    print(counter(string))