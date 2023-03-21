n=int(input())
for i in range(0,n):
    slen=int(input())
    s=input()
    sdict={}
    sdict[s[0]]=0
    sList=[]
    sList.append(0)
    prev=sList[-1]
    similarityFinder=0
    for j in range(1,len(s)):
        if s[j] in sdict:
            sList.append(sdict[s[j]])
        else:
            if prev ==1:
                sdict[s[j]]=0
                sList.append(0)
            else:
                sdict[s[j]]=1
                sList.append(1)
        if prev==sList[-1]:
            similarityFinder=1
            break
        else:
            prev=sList[-1]

    if similarityFinder==1:
        print("NO")
    else:
        print("YES")
