number = int(input("Enter a number: "))

def is_prime(num):
    if num < 2: 
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

result = is_prime(number)
print(result)