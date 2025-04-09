import sys
input = sys.stdin.readline

N = input().rstrip()
N_int = list(N)
count = 0
count_2 = 0

for T in range(0,len(N_int)-1):
    
    if N_int[T] != N_int[T+1]:
        count += 1
    
count +=1
count = count//2
print(count)