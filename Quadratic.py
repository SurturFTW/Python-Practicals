import cmath

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

x = (b ** 2) - (4 * a*c)

ans1 = (-b  -cmath.sqrt(x)) / (2 * a)
ans2 = (-b + cmath.sqrt(x)) / (2 * a)

print("Root one is ", ans1)
print("Other root is ", ans2)
