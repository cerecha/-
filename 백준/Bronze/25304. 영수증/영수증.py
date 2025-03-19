C = int(input())
N = int(input())
Finalcost = int(0)

for i in range(0,N):
    M, M2 = (map(int,input().split()))
    Finalcost += (M * M2)

if Finalcost == C:
    print('Yes')
else:
    print('No')