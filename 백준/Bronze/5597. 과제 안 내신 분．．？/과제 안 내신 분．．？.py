
import sys
input = sys.stdin.readline

S_list = [i for i in range(1,31)]

for z in range(28):
    S = int(input())
    S_list.remove(S)
    
print(min(S_list))
print(max(S_list))