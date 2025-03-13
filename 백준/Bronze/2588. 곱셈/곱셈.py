a = int(input()) #472
b = int(input()) #385

print(a * (b % 10)) #385 나누기 10의 나머지는 5
print(a * ((b // 10) % 10)) #
print(a * (b // 100))
print(a * b)