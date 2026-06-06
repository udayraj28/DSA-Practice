# check whether the given number is armstong number or not. 

n = int(input("Enter a number"))
num  = n
total = 0

power = len(str(n)) 

while (num > 0):
    last_digit = num % 10
    total = total + (last_digit ** power)
    num = num // 10
    
if(total == n):
    print(f"{n} is a Armstrong number")

else:
    print(f"{n} is not a Armstrong number")