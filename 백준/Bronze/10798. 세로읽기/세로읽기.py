import sys
input = sys.stdin.readline

word = [input().rstrip() for z in range(5)]
C_word = ''

for i in range(15):
  for j in range(5):
    if i <= len(word[j])-1:
      C_word += word[j][i]
print(C_word)