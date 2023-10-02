n, k = [int(s) for s in input().split()]
array = []
for s in range (n):
    array.append('I')
for i in range (k):
    l, r = [int(p) for p in input().split()]
    for u in range (l-1, r):
        array[u] = '.'
for elem in array:
    print(elem, end= '')