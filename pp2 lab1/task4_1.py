n = int(input())
chas = int(n // 60)
min = int(n % 60)
if chas < 24 & min < 60:
    print(chas, min)
else:
    a = int(chas // 24 )
    print(chas - (a * 24), min)