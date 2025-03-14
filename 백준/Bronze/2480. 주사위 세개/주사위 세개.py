
D= list(map(int,input().split()))

A = D.count(D[0])
B = D.count(D[1])
C = D.count(D[2])
Max = max(D)
Money1 = (10000+D[0]*1000) #전부 같은눈
#Money2 = (1000+*100) #2개 같은눈
Money3 = (Max *100) #모두 다른눈

if A == 3 or B == 3 or C ==3:
    print(Money1)
elif A == 2 or B ==2  or C ==2:
    if A == B:
        print((1000+D[0]*100))
    elif A == C:
        print((1000+D[0]*100))
    elif C == B:
        print((1000+D[2]*100))
    elif C == B:
        print((1000+D[2]*100))
    
    
else :
    print(Money3)