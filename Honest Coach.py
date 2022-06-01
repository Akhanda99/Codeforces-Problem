t=int(input())
for i in range(0,t):
    n=int(input())
    s=sorted(list(map(int, input().strip().split())))
    mindif=9999
    for j in range(0,n-1):
        if (s[j+1]-s[j])<mindif:
            mindif=s[j+1]-s[j]
    print(mindif)