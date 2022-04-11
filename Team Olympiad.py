n=int(input())
exp=list(map(int, input().strip().split()))

if exp.count(1) and exp.count(2) and exp.count(3) >0:
    possTeam=min([exp.count(1),exp.count(2),exp.count(3)])
    print(possTeam)
    for i in range(0,possTeam):
        team=[]
        team.append(exp.index(1)+1)
        team.append(exp.index(2)+1)
        team.append(exp.index(3)+1)
        exp[exp.index(1)] = 0
        exp[exp.index(2)] = 0
        exp[exp.index(3)] = 0
        print(' '.join(str(e) for e in team))
else:
    print(0)