import sys
input = sys.stdin.readline
resurt = []

N = int(input())
cards = set(map(int, input().split()))

M = int(input())
checks = list(map(int, input().split()))

result = []
for i in checks:
    if i in cards:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))
