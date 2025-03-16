
import sys

T = int(input())
C = int(0)

for i in range(1,T+1):
    C +=1
    A, B = list(map(int,(sys.stdin.readline().split())))
    
    print(f"Case #{C}: {A + B}")
