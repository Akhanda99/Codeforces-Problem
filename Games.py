t=int(input())
h=[]
a=[]
ans=0
for i in range(0,t):
    h_j,a_j=map(int, input().strip().split())
    h.append(h_j)
    a.append(a_j)
for i in range(0,len(h)):
    ans+=a.count(h[i])
print(ans)