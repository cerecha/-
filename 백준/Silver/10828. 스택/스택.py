
import sys
input = sys.stdin.readline
stack = []

NUM = int(input())

for i in range (NUM):
    stack_M = input().rstrip()
    
    if "push" in stack_M:
        stack.append(stack_M[5:])

    elif "top" in stack_M:
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)
        
    elif "empty" in stack_M:
        if len(stack) == 0:
            print(1)
        else :
            print(0)
        
    
    elif "size" in stack_M:
        print(len(stack))
    
    elif "pop" in stack_M:
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)

    
    

        

        
    
    
