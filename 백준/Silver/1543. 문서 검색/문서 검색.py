
import sys
input = sys.stdin.readline

S = input().rstrip()
A = input().rstrip()
n = 0
i = 0

while True:

    n = S.find(A,n)
    if n == -1:
        break
    i += 1
    n = n + len(A)
    
    
print(i)