
import sys
input= sys.stdin.readline

N,N_2=map(int,input().split())
arr=[]

for i in range(1,N+1):
    if(N%i==0):
        arr.append(i)

if(N_2<=len(arr)):
    print(arr[N_2-1])
else:
    print(0)


