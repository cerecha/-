
import sys
input = sys.stdin.readline
N_C = []
S = 0

N = int(input()) #횟수
N_C = input().split()#문자열로 받아옴
N_C = [int(N) for N in N_C] #받아온 문자열을 정수로 변환
V = int(input()) #타겟 되는 정수

for i in range(N):

    if N_C[i] == V:
        S += 1
    else:
        S += 0 
        
print (S)