number = int(input("Enter a number: "))

#print("built in method:", len(number)) 

count = 0
while number>0:
    number //= 10
    count += 1

print("Digit count:", count)