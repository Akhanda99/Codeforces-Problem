import math
n,k=map(int,input().strip().split())
req=240-k
count=0
treq=0
if req>0:
    for i in range(1,n+1):
        treq=5*i+treq
        if treq<=req:
            count+=1
        else:
            break

print(count)