
import sys
input = sys.stdin.readline
N, M = map(int,input().rstrip().split())

N_list = []
for _ in range(N):
  N_list.append(int(input()))

first = 1
last =  max(N_list)

while(first <= last):
  mid = (first + last) // 2
  list_C = 0

  for line in N_list:
    list_C +=  line // mid
    
  if list_C >= M:
    first = mid + 1
  else:
    last = mid - 1

print(last)