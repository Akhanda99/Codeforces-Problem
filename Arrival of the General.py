n = int(input())
hlist = list(map(int,input().split()))
maxH = 0
minH = n-1
for i in range(n):
	if hlist[i]> hlist[maxH]:
		maxH=i
	if hlist[i]<=hlist[minH]:
		minH = i
if minH>maxH:
	print (n+maxH-minH-1)
else:
	print (n+maxH-minH-2)