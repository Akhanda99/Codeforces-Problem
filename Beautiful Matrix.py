arr = []
r_pos = c_pos = 0
for _ in range(5):
    arr.append(list(map(int, input().rstrip().split())))
for i in range(0,5):
    for j in range(0,5):
        if arr[i][j]==1:
            r_pos=i
            c_pos=j
            break
result = abs(2-r_pos)+abs(2-c_pos)
print(result)
