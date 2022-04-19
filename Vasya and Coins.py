t=int(input())
for i in range(0,t):
    a,b=map(int, input().strip().split())
    if a>0:
        maxPay=a*1+b*2
    else:
        maxPay=0
    print(maxPay+1)
