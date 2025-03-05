length = int(input("Enter the length of the series: "))

a = 0
b = 1

print(a)
print(b)

for i in range(0, length-1):
    res = a + b
    print(res)
    a = b
    b = res

