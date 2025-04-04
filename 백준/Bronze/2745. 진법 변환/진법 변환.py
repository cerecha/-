
import sys
from collections import deque

input = sys.stdin.readline
dq = deque()

ALPA = ["0","1","2","3","4","5","6","7","8","9",
        "A","B","C","D","E","F","G","H","I","J",
        "K","L","M","N","O","P","Q","R","S","T",
        "U","V","W","X","Y","Z"]

N, B = input().rstrip().split()
B = int(B)

for ch in N:
    dq.append(ALPA.index(ch))

SUM = 0
P = 0
while dq:
    val = dq.pop()
    SUM += val * (B ** P)
    P += 1

print(SUM)