t=int(input())
flag=0
for i in range(0,t):
    flag = 0
    n=int(input())
    l=sorted(list(map(int, input().strip().split())))
    for j in range(0,n-1):
        if l[j+1]-l[j]>1:
            flag=1
            break
        else:
            continue
    if flag==1:
        print("NO")
    else:
        print("YES")