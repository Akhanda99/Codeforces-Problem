n=int(input())
coinList = list(map(int,input().split()))
coinList = sorted(coinList)
s = 0
c = 0
count =0
for i in coinList:
	s+=i

for i in coinList[::-1]:
	c+=i
	count+=1
	if c >(s/2):
		break

print(count)


