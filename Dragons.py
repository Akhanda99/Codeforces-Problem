s,n=map(int,input().strip().split())

l=[]
count=0
for i in range(0,n):
    x,y=map(int,input().strip().split())
    l.append((x,y))
    l.sort()
for i in range(0,len(l)):
    if s>l[i][0]:
        s += l[i][1]
        count+=1
        pass
    else:
        break
if count==len(l):
    print("YES")
else:
    print("NO")