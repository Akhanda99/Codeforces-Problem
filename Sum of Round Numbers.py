n=int(input())
for i in range(0,n):
    num=input()
    l=len(num)
    numSplit=""
    for j in range(0,l):
        if num[j]!=0:

            numSplit=num[j]
        else:
            numSplit=numSplit+num[j]

