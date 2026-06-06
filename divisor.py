# in this we check whether the given number is divisible by which numbers


a = int(input("Enter a Divisor:"))
num = a

result = []

for i in range (1, (num // 2) + 1):
    if num % i == 0:
        result.append(i)
    
result.append(num)   

print(f"{a} is divisible by {result} numbers")