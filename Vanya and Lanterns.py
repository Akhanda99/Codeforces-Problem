n,l=map(int,input().strip().split())
a=input().strip().split()
a=sorted(list(map(int,a)))
d=0.0

for i in range(0,len(a)-1):
    d=max(a[i+1]-a[i],d)

d=d/2

if a[0]!=0:
    d=max(d,a[0])
if a[n-1]!=l:
    d=max(d,l-a[n-1])

print(float(d))