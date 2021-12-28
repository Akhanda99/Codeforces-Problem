a = int(input())
b = int(input())
c = int(input())
ans = 0
if a+(b*c) > ans:
    ans = a+(b*c)
if a * (b+c) >ans:
    ans = a * (b+c)
if a*b*c > ans:
    ans = a*b*c
if (a+b)*c> ans:
    ans = (a+b)*c
if a+b+c >ans:
    ans = a+b+c
if a*(b+c) > ans:
    ans = a*(b+c)

print(ans)