a = [int(i) for i in input().split()]
prev = a[0]
for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(*a)