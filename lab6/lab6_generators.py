#1
def square_generator(N):
    for num in range(1, N + 1):
        yield num ** 2

#2
def even_numbers_generator(n):
    for num in range(n + 1):
        if num % 2 == 0:
            yield num

n = int(input("Enter a number:"))

even_numbers = even_numbers_generator(n)
even_numbers_list = list(even_numbers)
even_numbers_str = ', '.join(map(str, even_numbers_list))
print(even_numbers_str)

#3
def divisible_by_3_and_4(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

#4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = 4
b = 9
for square in squares(a, b):
    print(square)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1




