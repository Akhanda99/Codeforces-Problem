n=int(input())
box=list(map(int, input().strip().split()))
box.sort()

print(" ".join(str(i) for i in box))

