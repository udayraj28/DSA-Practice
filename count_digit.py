# Count the number of digits in the number given by user

n = int(input("Enter a number:"))
num = n
count = 0

while(num > 0):
    num = num // 10
    count = count + 1

print("total number of digits in the given number is:", count)
