
import sys
input = sys.stdin.readline

coin = [25, 10, 5, 1]
T = int(input())

for _ in range(T) :
    C = int(input())
    S = []

    for i in coin :
        S.append(C // i)
        C = C % i	
        
    print(*S)