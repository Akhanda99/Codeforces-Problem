import math
n=int(input())
for i in range(0,n):
    inp=int(input())
    if inp%2==0:
        print(math.floor(inp/2)-1)
    else:
        print(math.floor(inp/2))