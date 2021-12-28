t=int(input())
s=input()
a=s.count('A')

if a>abs(t-a):
    print("Anton")
elif a<abs(t-a):
    print("Danik")
else:
    print("Friendship")
