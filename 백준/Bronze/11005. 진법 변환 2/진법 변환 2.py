import sys

input = sys.stdin.readline

ALPA = ["0","1","2","3","4","5","6","7","8","9",
        "A","B","C","D","E","F","G","H","I","J",
        "K","L","M","N","O","P","Q","R","S","T",
        "U","V","W","X","Y","Z"]

N, B = input().rstrip().split()
N = int(N)
B = int(B)

SUM = []

while N:
    remainder = N % B
    SUM.append(ALPA[remainder])
    N = N // B

print(''.join(reversed(SUM)))