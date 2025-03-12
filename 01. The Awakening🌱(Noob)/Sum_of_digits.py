number = int(input("Enter a number:"))

result = 0
while number > 0:
    digit = number % 10
    print(digit)
    result = result + digit
    print(result)
    number //= 10
    print(number)

print("Sum of all the digits are: ",result)