

N1, N2 = map(int,input().split())

if N1!=0 and N2 !=0:
    print(N1+N2)
    N1, N2 = map(int,input().split())
    while N1!=0 and N2 !=0:
        print(N1+N2)
        N1, N2 = map(int,input().split())
