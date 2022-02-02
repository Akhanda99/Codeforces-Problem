n=int(input())
for i in range(0,n):
    a=input()
    data=""
    for j in range(0,len(a),2):
        if j==0:
            data=a[j]+a[j+1]
        else:
            data=data+a[j+1]
    print(data)

