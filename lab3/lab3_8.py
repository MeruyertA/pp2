a = input().split()
b = 1
for i in range(1, len(a)):
    if int(a[i-1])!=int(a[i]):
        b = b+1
print(b)