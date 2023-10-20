#1
class class1():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

#2
class Shape:
    def __init__(self):
        pass  

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

#3
class Rectangle(Shape):  
    def __init__(self, length, width):
        super().__init()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"coordinates are: ({self.x}, {self.y})")

    def move(self, moved_x, moved_y):
        self.x = moved_x
        self.y = moved_y

    def dist(self, point2):
        return ((self.x - point2.x)**2 + (self.y - point2.y)**2)**0.5
        
#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Now balance is {self.balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Now balance is {self.balance}")
        else:
            print("Error")

account1 = Account("Meruyert Adambay", 500000)

account1.deposit(100000)
account1.deposit(50000)
account1.withdraw(540000)
account1.withdraw(300000)
            
#6
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
only_prime = list(filter(lambda x: is_prime(x), num))
print(only_prime)



        

