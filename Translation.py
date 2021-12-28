word=input()
userinversword= input()

reverseWord = ''.join(reversed(word))
if reverseWord == userinversword:
    print("YES")
else:
    print("NO")