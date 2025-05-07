
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline


N = int(input().rstrip())
A = list(map(int,input().rstrip().split()))
A.sort()


M = input().rstrip()
X = list(map(int,input().rstrip().split()))



for i in X:
    print(bisect_right(A,i)-bisect_left(A,i),end=' ')