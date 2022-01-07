# runtime error -_-

n=int(input())
l=list(map(int,input().strip().split()))

for i in range(0,n):
    count = 2
    for j in range(2,(l[i]//2)+1):
        if l[i]%j==0:
            count+=1
            if count>3 or count<3:
                break
    if count==3:
        print("YES")
    else:
        print("NO")
