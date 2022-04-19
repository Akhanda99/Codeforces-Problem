t=int(input())
for i in range(0,t):
    n,k=map(int,input().strip().split())
    a=list(map(int, input().strip().split()))
    b=list(map(int,input().strip().split()))
    if max(b)<=min(a):
        print(sum(a))
    else:
        for j in range(0,k):
            a.append(max(b))
            b.append(min(a))
            a.remove(min(a))
            b.remove(max(b))
        print(sum(a))
