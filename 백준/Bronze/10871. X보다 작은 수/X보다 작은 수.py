
import sys
input = sys.stdin.readline

N, X = map(int,input().split()) #N과 X를 받아옴
A = [int(i) for i in input().split()] # A를 정수의 리스트로 받아옴
X_list = []

for i in range(N):
    if A[i] < X:
        X_list.append(A[i])
    
    else:
        pass

print(*X_list)