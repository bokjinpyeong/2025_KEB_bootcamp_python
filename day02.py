# for dan in range(2, 10, 1):
#     for i in range(1, 10, 1):
#         print(f"{dan}*{i} = {dan*i}")
# v1.1) for-> while
# v1.2) while 구문으로 구간 소수를 출력하는 프로그램을 작성
# v1.3) ** 대신 파워 함수 사용


n= int(input("Input number:"))

is_prime = False

while n>=2:

    #for i in range(2, n):
    #for i in range(2, int(n**0.5)+1):
    i=2
    while i<=int(n**0.5)+1:
        if n % i ==0:
            #count = count + 1
            is_prime = False
            break
else:
    is_prime=False

#if count ==0:
if is_prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number!")

