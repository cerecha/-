
from collections import deque
import sys

input = sys.stdin.readline
dq = deque()
N = input().rstrip()

for i in N:
    dq.append(i)

left = 0
right = 0

while len(dq) !=0:
    left += int(dq.pop())
    right += int(dq.popleft())

if left == right:
    print("LUCKY")
    
else:
    print("READY")
    