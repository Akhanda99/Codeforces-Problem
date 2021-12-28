n=int(input())
comment="I hate"
for i in range(2,n+1):
    if i%2==0:
        comment=comment+" that I love"
    else:
        comment=comment+" that I hate"
comment=comment+" it"

print(comment)