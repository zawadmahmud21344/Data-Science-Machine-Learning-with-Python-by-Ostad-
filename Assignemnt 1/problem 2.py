#Basic Calcualtor

# Take two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Take operator
operator = input("Enter operator (+, -, *, /): ")

# Perform calculation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"

# Show result
print("Result:", result)
