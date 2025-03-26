
import sys
input = sys.stdin.readline

NUM_list = []

for j in range (9):
    NUM = int(input().rstrip())
    NUM_list.append(NUM)
    
M = NUM_list.index(max(NUM_list))
print(max(NUM_list), M+1)
