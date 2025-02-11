# for dan in range(2, 10, 1):
#     for i in range(1, 10, 1):
#         print(f"{dan}*{i} = {dan*i}")

n = int(input("Input number:"))
count = 0
for i in range(1, n+1):
    if n % i ==0:
        count = count + 1

if count ==2:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number!")

