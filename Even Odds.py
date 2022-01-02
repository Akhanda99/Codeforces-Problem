import math
n,k=map(int,input().strip().split())

if math.ceil(n/2)>=k:
    ans=(2*(k-1))+1
elif math.ceil(n/2)<k:
    k=k-math.ceil(n/2)
    ans=(2*k)
print(ans)