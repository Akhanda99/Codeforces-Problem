s = input()
i=0
while i<len(s):
	if s[i:i+3] == "WUB":
		i+=3
	else:
		d =i
		while s[i:i+3] != "WUB" and i<len(s) :
			i+=1
		print(s[d:i])

