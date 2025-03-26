
import sys
input = sys.stdin.readline

n = int(input())
paper_list = [[0] * 101 for _ in range(101)]


for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper_list[i][j] = 1


a = 0
for i in paper_list:
    a += sum(i)

print(a)
    