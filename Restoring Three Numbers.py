x=sorted(list(map(int, input().strip().split())))
x2=x[1]
a=x[3]-x2
c=x[2]-a
b=x2-c
print(str(a)+" "+str(b)+" "+str(c))