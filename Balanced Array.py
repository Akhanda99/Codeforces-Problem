t=int(input())
for i in range(0,t):
    n=int(input())
    l=[]
    if (n/2)%2!=0:
        print("NO")
    else:
        for j in range(2,n+2,2):
            l.append(j)
        lsum=sum(l)
        for j in range(1,n-2,2):
            l.append(j)
        lsumfinal=sum(l)
        l.append(abs(lsum-(lsumfinal-lsum)))
        print("YES")
        l_string = ' '.join(str(e) for e in l)
        print(l_string)