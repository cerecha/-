
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

trees = list(map(int, input().rstrip().split()))

first = 0
last = max(trees)

result = 0
while first <= last:
    mid = (first + last) // 2
    sum = 0
    
    for i in trees:
        if i > mid:
            sum += i - mid
            
    if sum >= M:
        result = mid
        first = mid + 1
    else:
        last = mid - 1

print(result)