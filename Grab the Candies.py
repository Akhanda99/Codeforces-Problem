t=int(input())
for i in range(0,t):
    n=int(input())
    a= list(map(int,input().strip().split()))
    m=0
    b=0
    for j in range(0,len(a)):
        if a[j]%2==0:
            m+=a[j]
        else:
            b+=a[j]
    if m>b:
        print("YES")
    else:
        print("NO")
