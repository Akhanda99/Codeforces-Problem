n = int(input())
val = list(map(int,input().strip().split()))
ans = 0.0
for i in val:
	ans+=float(i)/n
print(ans)