
import sys
input = sys.stdin.readline
X = int(input())
line = 0
end = 0
 
while end < X:
    line += 1
    end += line
 
gap = end - X
mom = 1
son = 1
 
if line % 2 == 0:
    son = line - gap
    mom += gap
else:
    son += gap
    mom = line - gap
    
print(f'{son}/{mom}')