n=int(input())
listx=list(map(int,input().split()))
listy=list(map(int,input().split()))
levelSet=set(listx[1:]+listy[1:])

if len(levelSet)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")