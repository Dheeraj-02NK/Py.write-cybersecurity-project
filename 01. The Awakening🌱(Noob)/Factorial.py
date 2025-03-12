number = int(input("Enter a number:"))

def fact(num):
    if num == 0:
        return 1
    else: 
        return num * fact(num-1)
    
result = fact(number)
print("Factorial:", result)