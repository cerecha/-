FH,FM = map(int,input().split())
T = int(input())

TO = FM+T
FH += TO//60
FM = TO%60

if FH >23:
    FH -=24

print(FH,FM)
    