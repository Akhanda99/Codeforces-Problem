from math import *
t=int(input())
for i in range(0,t):
    count=0
    n,k=map(int,input().strip().split())
    if ceil(n/2)<k:
        print("-1")
    else:
        if k==ceil(n/2):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if i==j and i%2!=0:
                        if count<k:
                            print("R",end="")
                            count+=1
                        else:
                            print(".",end="")
                    else:
                        print(".",end="")
                print("\n",end="")
        else:
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if i==j and i%2==0:
                        if count < k:
                            print("R", end="")
                            count += 1
                        else:
                            print(".", end="")
                    else:
                        print(".",end="")
                print("\n",end="")