n=int(input())
giftNum=list(map(int,input().strip().split()))
sequencedlist=[]
index=0
for i in range(1,len(giftNum)+1):
    for j in range(0,len(giftNum)):
        if giftNum[j]==i:
            index=j
    sequencedlist.append(str(index+1))
print(" ".join(sequencedlist))


