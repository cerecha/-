
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


N = int(input().rstrip())
A = list(map(int,input().rstrip().split()))
A.sort()



M = input().rstrip()
X = list(map(int,input().rstrip().split()))

for i in X:
    if bisect_left(A,i) >= len(A):
        print(0)
    else:
        if A[bisect_left(A,i)] == i:
            print(1)
        else:
            print(0)