n=int(input())
for i in range(0,n):
    num=input()
    l=len(num)
    listofSplitNum=[]
    for j in range(0,l):
        if num[j]!='0':
            splitnum=num[j]+("0"*(l-j-1))
            listofSplitNum.append(splitnum)
    print(len(listofSplitNum))
    print(" ".join(listofSplitNum))
