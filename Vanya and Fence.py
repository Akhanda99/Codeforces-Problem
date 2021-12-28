num,hfence=map(int,input().strip().split())
hfriend=list(map(int,input().strip().split()))
width=0
for i in range(0,num):
    if hfriend[i]>hfence:
        width+=2
    else:
        width+=1
print(width)