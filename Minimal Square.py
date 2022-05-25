t=int(input())
for i in range(0,t):
    a,b=map(int,input().strip().split())
    if a>=b:
        maxVal=max(a,b*2)
    else:
        maxVal=max(b,a*2)
    print(maxVal**2)
            