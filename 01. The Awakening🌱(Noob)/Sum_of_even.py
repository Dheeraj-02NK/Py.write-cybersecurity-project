length = int(input("Enter the length of the series: "))

sum = 0

for i in range(1, length+1):
    if i%2 == 0:
        sum = sum + i

print(sum)