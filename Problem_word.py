n=input()
count=0

for i in range(0,len(n)):
    if n[i].isupper():
        count+=1
    else:
        pass

if count>abs(count-len(n)):
    n=n.upper()
else:
    n=n.lower()

print(n)
