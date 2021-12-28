n,m=map(int,input().strip().split())
puzzleList=sorted(list(map(int,input().split())))
minDif=9999
for i in range(m):
    if (i+(n-1)) <= m-1 and abs(puzzleList[i]-puzzleList[i+(n-1)])< minDif:
            minDif=abs(puzzleList[i]-puzzleList[i+(n-1)])
print(minDif)