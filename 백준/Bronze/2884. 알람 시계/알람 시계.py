H, M = map(int, input().split())

if M < 45:
    if H ==0:
        H=23
        M+=60
    else :
        M+=60
        H-=1
    
print(H,M-45)