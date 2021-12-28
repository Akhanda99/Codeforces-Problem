forceNumber = int(input())
forceValue=[]
for i in range(forceNumber):
    forceValue.append(list(map(int,input().strip().split())))
count = 0

for i in range(0,3):
    sum=0
    for j in range(0,forceNumber):
        sum = sum+ forceValue[j][i]
    if sum==0:
        count+=1

if count==3:
    print("YES")
else:
    print("NO")