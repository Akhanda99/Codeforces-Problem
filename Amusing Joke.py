guest=input()
host=input()
pile=input()
gh=guest+host
ghset=sorted(set(gh))
pileset=sorted(set(pile))
count=0

if len(ghset)==len(pileset):
    for i in ghset:
        if gh.count(i)==pile.count(i):
            count+=1
            continue

if count==len(ghset):
    print("YES")
else:
    print("NO")