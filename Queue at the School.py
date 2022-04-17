n,t=map(int,input().strip().split())
s=list(input())
for i in range(0,t):
    j=0
    while (j<n-1):
        if s[j]=='B' and s[j+1]=='G':
            s[j],s[j+1]=s[j+1],s[j]
            j+=2
        else:
            j+=1
print("".join(str(e) for e in s))