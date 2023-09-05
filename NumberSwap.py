a = 2
b = 3

#Number swap without 3rd variable
a, b = b, a
print("Without using third variable")
print("a = ", a, " and ", "b = ", b)

#Number swap using 3rd variable
temp = a
a = b
b = temp
print("Using third variable")
print("a = ", a, " and ", "b = ", b)
