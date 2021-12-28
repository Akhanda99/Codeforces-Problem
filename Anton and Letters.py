s=set(input())
sr={"{"," ","}",","}
if len(s.difference(sr))>0:
    print(len(s.difference(sr)))
else:
    print("0")