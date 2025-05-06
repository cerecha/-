
import heapq
import sys
input = sys.stdin.readline

n = int(input())
cards = []

for _ in range(n):
    num = int(input().rstrip())
    heapq.heappush(cards, num)

total = 0

while len(cards)>1:
    n_1 = heapq.heappop(cards)
    n_2 = heapq.heappop(cards)
    total += n_1 + n_2
    heapq.heappush(cards, n_1+n_2)

print(total)