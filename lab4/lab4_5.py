n, m = map(int, input(). split())
anya = set()
boris = set()
for i in range (n):
    color = int(input())
    anya.add(color)
    
for i in range(m):
    color = int(input())
    boris.add(color)

common = anya.intersection(boris)
only_anya = anya.difference(boris)
only_boris = boris. difference(anya)

print(len(anya&boris))
print(*sorted(anya&boris))

print(len(anya - boris))
print(*sorted(anya - boris))

print(len(boris - anya))
print(*sorted(boris - anya))


