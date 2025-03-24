       
import sys
input = sys.stdin.readline

TC = int(input().rstrip())

for i in range(TC):
    case = str(input().rstrip())
    score = 0
    c = 0
    for j in list(case):
        if j == "O":
            c += 1
            score += c
        elif j == "X":
            c = 0
    print(score)