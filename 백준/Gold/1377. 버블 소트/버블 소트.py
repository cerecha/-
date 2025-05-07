import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = []
for i in range(N):
    arr.append((int(input().rstrip()), i))

arr.sort()

count = 0
for j in range(N):
    k = arr[j][1] - j
    if k > count:
        count = k

        
print(count + 1)