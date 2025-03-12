len = int(input("Enter the number of elements: "))

elements = []
print("Enter", len, "elements: ")
for i in range(1, len+1):
    ele = int(input())
    elements.append(ele)

highest = 0
for i in range(0, len):
    if elements[i] > highest:
        highest = elements[i]


print("Inbuilt method:", max(elements))
print("Logic method:", highest)
