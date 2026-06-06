# we have to check whether the given number by user is palindrome or not

n = int(input("Enter a number:"))
num = n
result = 0

while(num > 0):
    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num // 10

if (n == result):
    print(f"{n} is palindrome")

else:
    print(f"{n} is not palindrome")
