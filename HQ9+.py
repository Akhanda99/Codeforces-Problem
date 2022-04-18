p=input()
flag=0
for i in range(0,len(p)):
    if p[i]=='H' or p[i]=='Q' or p[i]=='9':
        flag=1
        break
if flag==0:
    print("NO")
else:
    print("YES")