x=int(input())
j=1
num_of_bact=1
while True:
    if x==1:
        print(num_of_bact)
        break
    else:
        if x%2==0:
            x=x/2
        else:
            num_of_bact+=1
            x=x-1
