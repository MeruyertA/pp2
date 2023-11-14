#1
from functools import reduce

def multip(numbers):
    return reduce(lambda x, y: x * y, numbers)

list1 = [2, 3, 4, 5]
result = multip(list1)
print(result)

#2
def count_letters(input_string):
    upp_c = sum(map(str.isupper, input_string))
    low_c = sum(map(str.islower, input_string))
    return upp_c, low_c

str1 = "Hello World"
upper, lower = count_letters(str1)
print("Upper case count:", upper)
print("Lower case count:", lower)

#3
def is_palindrome(str1):
    return str1 == str1[::-1]

str2 = "radar"
if is_palindrome(str2):
    print("This string is a palindrome")
else:
    print("This string is not a palindrome")

#4
import time
from math import sqrt

def square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = sqrt(number)
    return result

num = 25100
milliseconds = 2123
sqrt_result = square_root(num, milliseconds)
print(f"Square root of {num} after {milliseconds} milliseconds is {sqrt_result}")


#5
def elem_true(tup):
    return all(tup)

tup1 = (True, True, False, True)
if elem_true(tup1):
    print("All elements in the tuple are True.")
else:
    print("Some elements in the tuple are False.")
