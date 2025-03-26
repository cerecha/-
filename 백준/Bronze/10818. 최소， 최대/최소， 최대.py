
import sys
input = sys.stdin.readline

N = int(input())
NUM = [int(i) for i in input().split()]
NUM.sort()
M = max(NUM)
MI = min(NUM)
print(MI, M)
