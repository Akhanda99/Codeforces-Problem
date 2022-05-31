t=int(input())
for i in range(0,t):
    k=int(input())
    count=0
    for j in range(1,k+1):
        count+=1
        while True:
            if count%3==0 or str(count)[-1]=='3':
                count+=1
            else:
                break
            
        print(j,count)
    print(count)
        