# for dan in range(2, 10, 1):
#     for i in range(1, 10, 1):
#         print(f"{dan}*{i} = {dan*i}")
# v1.1) for-> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램을 작성
# v1.3) ** 대신 파워 함수 사용

#결과  n1<숫자<n2 중 소수들 print
# n1과 n2 사이의 숫자가 모두 반복문 사이에 들어가야 한다.
#반복하는데 n1+1부터 시작해서 n2-1까지 반복



number1= int(input("Input number1:")) # 4
number2= int(input("Input number2:"))  # 8

between_number=number1+1
is_prime = False

while number1<=between_number<=number2:   # 4<= <=8


    while between_number>= 2:
        i = 2
        while i <= int(between_number ** 0.5) + 1:
            if between_number % i == 0:
                print(between_number)















