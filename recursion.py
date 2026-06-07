# when a function calls itself again and again then it is known as recursion function

# print uday 10 times using recursion

count = 0
def func():
    global count  # declare variable count as global 
    if count == 10:
        return
    
    print("Uday")
    count = count + 1
    func()

func()