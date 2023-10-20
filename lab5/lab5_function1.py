#1
def ounces_to_grams(ounces):
    grams = ounces * 28.3495231
    return grams

ounces = float(input())
grams = ounces_to_grams(ounces)
print(grams)

#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

fahrenheit = float(input())
celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)

#3
def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return None

numheads = 35
numlegs = 94

result = solve(numheads, numlegs)

if result is not None:
    num_chickens, num_rabbits = result
    print(num_chickens)
    print(num_rabbits)
else:
    print("Error")
    
#4
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    prime_numbers = filter(is_prime, numbers)
    return list(prime_numbers)

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter_prime(numbers)
print(prime_numbers)

#5
from itertools import permutations

def permut(str1):
    per = permutations(str1)
    for i in per:
        print(''.join(i))

str = input("")

permut(str)

#6
def reverse_words(str1):
    words = str1.split()
    rev = ' '.join(reversed(words))
    return rev

str1 = input()
rev = reverse_words(str1)
print(rev)

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8
def spy_game(nums):
    code = [0, 0, 7]
    index = 0

    for num in nums:
        if num == code[index]:
            index += 1
            if index == len(code):
                return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

#9
import math

def sphere_volume(radius):
    if radius < 0:
        return "Error"
    
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

radius = float(input())
volume = sphere_volume(radius)
print(volume)

#10 
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


#11 
def is_palindrome(text):
    clean_text = ''.join(text.split()).lower()
    return clean_text == clean_text[::-1]

word = input()
if is_palindrome(word):
    print("palindrome")
else:
    print("not a palindrome")

#12
def histogram(int_list):
    for num in int_list:
        print('*' * num)

user_input = input()
int_list = [int(item) for item in user_input.split()]

histogram(int_list)

#13
import random

def guess_the_number():
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses = 0
    while True:
        try:
            guess = int(input("Take a guess: "))
            guesses += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
                break
        except ValueError:
            print("Enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
#14
import random

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def is_palindrome(text):
    clean_text = ''.join(text.split()).lower()
    return clean_text == clean_text[::-1]

def guess_the_number():
    secret_number = random.randint(1, 20)

    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses = 0
    while True:
        try:
            guess = int(input("Take a guess: "))
            guesses += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

input_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]
result_list = unique_elements(input_list)
print("Unique elements:", result_list)


word = "racecar"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")


guess_the_number()

























