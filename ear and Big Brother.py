
lweight,lbob=map(int,input().strip().split())
year_count=0
while True:
    lweight=lweight*3
    lbob=lbob*2
    year_count+=1
    if lweight>lbob:
        print(year_count)
        break