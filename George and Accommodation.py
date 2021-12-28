numRoom=int(input())
count=0
for i in range(0,numRoom):
    nStudent,cp=map(int,input().strip().split())
    if cp-nStudent>=2:
        count+=1
    else:
        pass
print(count)