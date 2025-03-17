import sys
N1, N2 = map(int,sys.stdin.readline().split())

while True : 
    try:
        print(N1+N2)
        N1, N2 = map(int,input().split())
    
    except:
	    
        break