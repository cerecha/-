
   
import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = []

for i in range(N):
    n,i1,i2,i3 = map(str,input().rstrip().split())
    arr.append([n,int(i1),int(i2),int(i3)])
    
arr = sorted(arr, key = lambda x:(-x[1],x[2],-x[3],x[0]))
for j in (arr):
    print(j[0])
