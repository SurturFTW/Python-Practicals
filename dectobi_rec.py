# Decimal to binary conversion using recursion
def find( decimal_number ):
	if decimal_number == 0:
		return 0
	else:
		return (decimal_number % 2 + 10 *
				find(int(decimal_number // 2)))

# Driver Code
decimal_number = int(input("Enter a decimal number: "))
print("Binary equivalent is ", find(decimal_number))
