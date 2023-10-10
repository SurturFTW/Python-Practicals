# main.py
import calculator

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter operation (1/2/3/4): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        result = calculator.add(num1, num2)
        print(f"Result: {result}")
    elif choice == '2':
        result = calculator.subtract(num1, num2)
        print(f"Result: {result}")
    elif choice == '3':
        result = calculator.multiply(num1, num2)
        print(f"Result: {result}")
    elif choice == '4':
        result = calculator.divide(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
