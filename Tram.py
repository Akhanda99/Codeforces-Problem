t= int(input())
numberPass=[]
numberOfPass=0
for i in range(0,t):
    exit, inter=map(int, input().strip().split())
    numberOfPass=numberOfPass-exit+inter
    numberPass.append(numberOfPass)
print(max(numberPass))