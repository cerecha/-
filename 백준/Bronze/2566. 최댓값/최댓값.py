import sys
input = sys.stdin.readline

A = []

for i in range(9):
    A.append(list(map(int, input().split())))

max_v = -1
row_v = 0
c = 0

for i in range(9):
    for j in range(9):
        if A[i][j] > max_v:
            max_v = A[i][j]
            row_v = i+1
            c = j+1

print(max_v)
print(row_v, c)