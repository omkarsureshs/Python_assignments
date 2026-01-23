def factorial():
    """Calculate the factorial of a number."""
    num = int(input("Enter a number to calculate its factorial: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
        return
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f"The factorial of {num} is : {result}")

if __name__ == "__main__":
    factorial()