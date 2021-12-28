a=input()
b=input()
ans=""
for i in range(0,len(a)):
    if a[i]==b[i]=="1" or a[i]==b[i]=="0":
        ans=ans+"0"
    else:
        ans=ans+"1"
print(ans)