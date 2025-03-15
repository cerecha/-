
T = int(input()) #몇번 계산을 할건지 입력



for i in range(1,T+1): # i를 T번 반복
    N = list(map(int,(input().split()))) #계산할 정수를 리스트로 받아옴
    S = N[0]+N[1]
    
    print (S)