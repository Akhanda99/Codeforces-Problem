n=int(input())
opinion= list(map(int,input().strip().split()))
if opinion.count(1)>0:
    print("HARD")
else:
    print("EASY")