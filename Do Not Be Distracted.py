t=int(input())
for i in range(0,t):
    n=int(input())
    str_=input()
    str_list=[]
    str_list.append(str_[0])
    flag=0
    for j in range(0,n):
        if str_[j]==str_list[-1]:
            flag=1
        else:
            if str_list.count(str_[j])==1:
                flag=0
                break
            else:
                str_list.append(str_[j])
                flag=1
    if flag==0:
        print("NO")
    else:
        print("YES")


