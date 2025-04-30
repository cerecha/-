import sys
input = sys.stdin.readline


N = int(input().rstrip())
arr = [0] * 100001

for i in range(N):
    num = int(input().rstrip())
    arr[num] += 1
    
for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)
    
    







