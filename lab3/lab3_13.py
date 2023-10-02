a = [int(s) for s in input().split()]
n = 0
for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            n += 1
print(n)