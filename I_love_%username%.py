n=int(input())
point=list(map(int, input().strip().split()))
count=0
pset = []
pset.append(point[0])
for i in range(1,n):
    pset.append(point[i])
    if max(pset)==point[i] or min(pset)==point[i]:
        if pset.count(point[i]) == 1:
            count+=1
print(count)