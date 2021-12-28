n=int(input())
d=[100,20,10,5,1]

remaining=n
ans=0

for i in d:
    ans+=int(remaining/i)
    remaining= remaining%i
    
print(ans)
