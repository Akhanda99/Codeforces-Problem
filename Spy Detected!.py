t=int(input())
for i in range(0,t):
    n=int(input())
    a=list(map(int,input().strip().split()))
    a_com=list(set(a))
    for j in range(0,2):
        if a.count(a_com[j])==1:
            print(a.index(a_com[j])+1)
        else:
            continue
