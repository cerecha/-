
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = sorted(list(map(int,input().rstrip().split())))
h = (n-1)//2
print(arr[h])