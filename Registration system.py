t = int(input())
nameDic = {}

for i in range(0,t):
    name= input()
    if name in nameDic:
        print(name+ str(nameDic[name]))
        nameDic[name]+=1
    else:
        print("OK")
        nameDic[name]=1