
import sys
input= sys.stdin.readline


num=int(input())
d=2 
                
while True:
    if num==1:            
        break
    elif num==d:    
        print(num)
        break
    elif num%d!=0:  
        d+=1
        continue
    elif num%d==0 and (num%(d**2))==0: 
        num=num//d
        print(d)
        continue
    else:                    
        num=num//d
        print(d)
        d+=1
