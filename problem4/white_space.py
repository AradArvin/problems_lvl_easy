


def cap_space(text):
    for i in text:
        if i.isupper():
            text = text.replace(i, " " + i).strip()
            
    return text




if __name__ == "__main__":
    text = input("Please Enter a string: ")
    result = cap_space(text)
    print(result)


# One line version
#print(''.join(' ' + i if i.isupper() else i.strip() for i in text).strip())