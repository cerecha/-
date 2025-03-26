
import sys
input = sys.stdin.readline


N, M = map(int,input().split())  # 바구니 개수와 공을 넣을 줄의 개수

basketball_list =[0] * N

for x in range(M): # 몇개의 줄에 공을 넣을건지
    i, j, k = map(int,input().rstrip().split()) #공을 넣을 바구니의 범위와 공의 번호
    for z in range(i-1,j):
        basketball_list[z] = k

print(*basketball_list)
