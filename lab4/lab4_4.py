A = input().split()
was_before = set()
for i in A:
    if i in was_before:
        print("YES")
    else:
        was_before.add(i)
        print("NO")
