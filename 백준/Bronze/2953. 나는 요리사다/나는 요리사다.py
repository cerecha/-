
import sys
input = sys.stdin.readline

SN = []

for i in range(1, 6):
    S = list(map(int,input().rstrip().split()))
    N = S[0]+S[1]+S[2]+S[3]
    SN.append(N)
    
print(SN.index(max(SN))+1, max(SN))