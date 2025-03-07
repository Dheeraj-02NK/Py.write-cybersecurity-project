a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

maximum = max(a,b,c)
print(maximum)

if a>=b and a>=c:
    print(a,'is greater')
elif b>=c:
    print(b, 'is greater')
else:
    print(c, 'is greater')
