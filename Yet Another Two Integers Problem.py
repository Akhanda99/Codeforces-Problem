from math import *
t=int(input())
for i in range(0,t):
    a,b=map(int, input().strip().split())
    print(ceil(abs(a-b)/10))