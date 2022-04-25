import math
t=int(input())
for i in range(0,t):
    x,y,n=map(int, input().strip().split())
    a=math.floor(n/x)
    k=(a*x)+y
    while True:
        if (a*x)+y<=n:
            k = (a * x) + y
            print(k)
            break
        else:
            a-=1