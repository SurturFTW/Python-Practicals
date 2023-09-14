# With cmath module
'''import cmath

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

x = (b ** 2) - (4 * a*c)

ans1 = (-b  -cmath.sqrt(x)) / (2 * a)
ans2 = (-b + cmath.sqrt(x)) / (2 * a)

print("Root one is ", ans1)
print("Other root is ", ans2)
'''

# Without cmath module
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
x = (b ** 2) - (4 * a * c)
y = x ** 0.5
if x < 0:
   print("The roots are imaginary.")
else:
   ans1 = (-b - y) / (2 * a)
   ans2 = (-b + y) / (2 * a)
   print("Root one is ", round(ans1, 2))
   print("Other root is ", round(ans2, 2))
