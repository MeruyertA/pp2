a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
ind=0
for i in range(len(a)+1):
    if i!=b[0]:
        print(a[i-ind],end=' ')
    else:
        print(b[1],end=' ')
        ind+=1