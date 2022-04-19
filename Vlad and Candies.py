t=int(input())
for i in range(0,t):
    n=int(input())
    a=sorted(list(map(int, input().strip().split())))
    if n>1:
        if (a[-1]-a[-2])<=1:
            print("YES")
        else:
            print("NO")
    else:
        if a[0]>1:
            print("NO")
        else:
            print("YES")