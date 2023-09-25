a = int(input())
b = int(input())
c = int(input())

if (c % a == 0 and c <= a * b) or (c % b == 0 and c <= a * b):
    print("YES")
else:
    print("NO")