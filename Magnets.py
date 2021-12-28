n=int(input())
magnetType=[]
magType=0
count=0
for i in range(0,n):
    value=int(input())
    magnetType.append(value)
    if len(magnetType)==1:
        magType=magnetType[0]
        count+=1
    if len(magnetType)>1:
        if magnetType[i]==magType:
            pass
        else:
            count+=1
        magType=magnetType[i]
print(count)