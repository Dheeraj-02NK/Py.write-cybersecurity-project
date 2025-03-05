result = ''
number = input("Enter a number: ")

for i in range(len(number)-1,-1,-1):
    result = result+number[i]

result = int(result)
print(int(result))
print(type(result))