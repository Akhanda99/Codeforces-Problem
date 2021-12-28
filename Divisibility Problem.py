from math import *
t=int(input())

for i in range(0,t):
    a,b=map(int,input().split())
    ans= abs((ceil(a/b)*b)-a)
    print(ans)