number = int(input("Enter a number: "))

digit = 0
rev_number = 0
#i = 1

while number>0:
    #print("step-", i)
    digit = number % 10
    #print("digit:", digit)
    rev_number = rev_number*10 + digit
    #print("reverse:", rev_number)
    number //= 10
    #print("number:", number)
    #i+=1

print(rev_number)