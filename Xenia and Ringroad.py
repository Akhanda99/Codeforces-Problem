n,m=map(int, input().strip().split())
a=list(map(int,input().strip().split()))
pos=1
count=0
for i in range(0,m):
    if a[i]>pos:
        count+=abs(a[i]-pos)
    elif a[i]<pos:
        count+=n-abs(a[i]-pos)
    else:
        count+=0
    pos = a[i]
count+=abs(a[m-1]-pos)
pos=a[m-1]
print(count)