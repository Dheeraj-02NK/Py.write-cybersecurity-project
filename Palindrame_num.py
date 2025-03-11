number = int(input("Enter a number:"))

def is_palindrome(num):
    digit = 0
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

reverse = is_palindrome(number)

if number == reverse:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")