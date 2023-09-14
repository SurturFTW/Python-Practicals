principal = int(input("Enter principal amount: "))
interest = int(input("Enter interest rate: "))
time = int(input("Enter the duration: "))

amount = principal * pow(1 + interest / 100, time)
CI = amount - principal 
print("The compound interest is", CI)
