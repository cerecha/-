
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basket = list(range(1, N+1))

for z in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = reversed(basket[i-1:j])

print(*basket)
  