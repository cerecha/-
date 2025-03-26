

import sys
input = sys.stdin.readline

N , M = map(int,input().split())
basket_list = [1] * N


for z in range(N): #바구니와 바구니 안에 있는 공의 번호 지정
    basket_list[z] = z+1

for x in range(M): #공 교환식
    i, j = map(int,input().split()) # 바꿀 바구니의 번호를 가져옴
    
    basket_list[i - 1], basket_list[j - 1] = basket_list[j - 1], basket_list[i - 1]

print(*basket_list)

