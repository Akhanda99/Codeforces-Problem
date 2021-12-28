k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
setVal=set()
for i in range(1,d+1):
    if i%k==0:
        setVal.add(i)
    if i%l==0:
        setVal.add(i)
    if i % m == 0:
        setVal.add(i)
    if i % n == 0:
        setVal.add(i)

print(len(setVal))