# Normal method with built-in methods
from functools import reduce    # reduce() Applies a function to the list
from operator import mul        # mul is The multiplication operator function 
                                # reduce(mul, list)


def facto_func(num):

    if num == 0:
          return num + 1
    
    number_to_list = list(i+1 for i in range(num))
    result = reduce(mul, number_to_list)

    return result

if __name__ == "__main__":
	num = int(input("Enter a number: "))

	print(f"The factorial of {num} is : {facto_func(num)}")
      

# Ther is a bult-in python function from math library that can solve factorial as well.
      # import math -> math.factoraial(number)