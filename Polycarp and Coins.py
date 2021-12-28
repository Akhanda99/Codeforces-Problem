import math
n=int(input())
for i in range(0,n):
    t=int(input())
    ans=t/3
    if math.floor(ans)+(math.ceil(ans)*2)==t:
        print(str(math.floor(ans))+" "+str(math.ceil(ans)))
    else:
        print(str(math.ceil(ans))+" "+ str(math.floor(ans)))