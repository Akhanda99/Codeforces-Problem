t=int(input())
for i in range(0,t):
    n=int(input())
    a=list(map(int, input().strip().split()))
    even=0
    odd=0
    for j in range(0,n):
        if a[j]%2==j%2:
            continue
        else:
            if a[j]%2==0:
                even+=1
            else:
                odd+=1
    if even==odd:
        print(even)
    else:
        print(-1)