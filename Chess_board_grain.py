boxes = int(input("Enter the number of boxes: "))

res = 1
for i in range(1, boxes):
    res = res*2

print(res)