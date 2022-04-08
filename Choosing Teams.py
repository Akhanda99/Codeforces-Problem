n,k=map(int, input().strip().split())
count=0
y=list(map(int, input().strip().split()))
for i in range(0,n):
    if y[i]+k<=5:
        count+=1
    else:
        continue
print(count//3)