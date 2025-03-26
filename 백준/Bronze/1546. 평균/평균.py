
import sys
input = sys.stdin.readline

n = int(input())
S = list(map(int,input().split()))
avg_list = []
for i in range(n):
    n_max = max(S)
    avg_list.append((S[i] / n_max) * 100)
    
avg_sum = sum(avg_list)
avg_l = avg_sum / n
print(avg_l)
  