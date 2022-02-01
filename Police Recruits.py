n=int(input())
l=list(map(int,input().strip().split()))
m=count=0
for i in range(0,n):
    m=l[i]+m
    if m<0:
        count+=1
        m=0
print(count)