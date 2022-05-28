t=int(input())
for i in range(0,t):
    n=int(input())
    k=0
    param=0
    ansList=[]
    while True:
        param+=2**k
        
        if param>n:
            break
        
        else:    
            ans=n//param
            k+=1
            if ans*param==n:
                ansList.append(ans)
            else:
                continue

    print(max(ansList[1:]))