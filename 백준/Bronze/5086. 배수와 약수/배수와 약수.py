import sys
input= sys.stdin.readline
while 1:
    N_1, N_2 = map(int, input().rstrip().split())
    if N_1 == 0 and N_2 == 0:
        break
    
    elif N_2%N_1 == 0:
        print('factor')
    elif N_1%N_2 == 0:
        print('multiple')
    elif N_1%N_2 !=0 and N_2%N_1 != 0:
        print('neither')


