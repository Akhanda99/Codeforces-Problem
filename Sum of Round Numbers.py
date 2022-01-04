n=int(input())
for i in range(0,n):
    num=input()
    l=len(num)
    listofnum=[]
    for j in range(0,l):
        if num[j]!='0':
            splitnum=num[j]+("0"*(l-j-1))
            listofnum.append(splitnum)
    print(len(listofnum))
    print(" ".join(listofnum))
