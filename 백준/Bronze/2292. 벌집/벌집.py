
import sys
input = sys.stdin.readline

P = int(input())

N = 1
C = 1
while C < P:
    C += 6 * N
    N += 1

print(N)