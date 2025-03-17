# This script calculates the factorial of a given number using a loop

num = int(input("Enter a number to find its factorial: "))  # Taking user input
factorial = 1  # Initializing factorial variable

for i in range(1, num + 1):  # Loop from 1 to num
    factorial *= i  # Multiply each number to factorial

print(f"Factorial of {num} is {factorial}")  # Printing the result
