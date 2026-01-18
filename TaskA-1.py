num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
division_result = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {prod_result}")
print(f"Division: {division_result}")