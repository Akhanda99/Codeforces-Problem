hList=list(map(int, input().strip().split()))
count=0
for i in set(hList):
    if hList.count(i)>1:
        count=count+(hList.count(i)-1)
print(count)