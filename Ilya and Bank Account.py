acc_state=list(input())

if '-' in acc_state:
    if len(acc_state)>=3:
        acc_state.remove(max(acc_state[-1],acc_state[-2]))
    else:
        acc_state=['0']

acc_state=int("".join(str(e) for e in acc_state))
print(acc_state)