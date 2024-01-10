# Add White space before capital letters

This problem can be solved in many ways but the best way is the clean and short version. which is by using built in methods. 
all you need to do is make sure, in the output string there is a whitespace before capitall letters.


## Problem:

Take an input string from user and return the string with white spaces before capital letters, and make sure there is no white spaces at the start and the end of output string.


**Examples:**

1. input = "TheFirstLetter"
    - output = "The First Letter" 

2. input = "NeverLetMeGo"
    - output = "Never Let Me Go"


## Solution:

This problem is easily solveable with built in methods: isupper(), replace(), strip().
- isupper() > checks to see if a character in string is an upper-case(capital) letter.
- replace() > replaces a character in a string with another given character.
- strip() > strips the string from white spaces in the start and the end of string.
    
> lstrip() and rstrip() methods can be used too.
>    - lstrip() -> deletes whitespaces on the left side of string.
>    - rstrip() -> deletes whitespaces on the right side of string.


```bash
def cap_space(text):
    for i in text:
        if i.isupper():
            text = text.replace(i, " " + i).strip()
            
    return text
```

Here we use a for loop to iterate over the input string and then we set the condition `if i.isupper():` to see if a character is an upper case. if True then in the upper letter is replaced with `" " + i` a white space then the upper letter itself. finally strip method is used to delete any white spaces at the start or end of string, and the result string is returned.

In the end the result is printed to stdout.

```bash
result = cap_space(text)
print(result)
```

**Important Note:**
- This whole problem can be solved in one line of code. it basically does the same thing but in less lines of code. here is the one line solution:

```bash
text = "NeverLetMeGo"
print(''.join(' ' + i if i.isupper() else i.strip() for i in text).strip())
```

link to solution file:
[White spaces solution](white_space.py)


## Tests:

Tests are performed with diffrent inputs.

link to test file:
[White spaces test](test_white_space.py)

- in order to run tests pls make sure that **pytest** is installed on your environment. Then use `pytest -v` command to run tests in verbose mode.