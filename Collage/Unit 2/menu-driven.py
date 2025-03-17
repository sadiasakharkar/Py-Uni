# 5.Program to perform addition, subtraction, division and multiplication of given two numbers (menu driven)

'''
Problem Statement
Write a menu-driven program that takes two numbers as input and allows the user to perform the following operations:

Addition
Subtraction
Multiplication
Division
The user should be able to choose an operation from the menu, and the program should display the result accordingly.

Input
Two numbers (integer or floating-point).
A choice from the menu (1-4).
Output
The result of the chosen operation.
Example 1
Input:

Enter first number: 10  
Enter second number: 5  
Choose operation:  
1. Addition  
2. Subtraction  
3. Multiplication  
4. Division  
Enter your choice: 1  
Output:

Result: 15
Example 2
Input:

Enter first number: 8  
Enter second number: 2  
Choose operation:  
1. Addition  
2. Subtraction  
3. Multiplication  
4. Division  
Enter your choice: 4  
Output:

Result: 4.0
Constraints
The second number should not be zero for division.
The choice should be between 1 and 4; otherwise, an error message should be displayed.
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Choose Operation: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
choice = int(input("Enter your choice: "))

if choice == 1:
    result = num1 + num2
    print("Result: ", result)
elif choice == 2:
    result = num1 - num2
    print("Result: ", result)
elif choice == 3:
    result = num1 * num2
    print("Result: ", result)
elif choice == 4:
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result: ", result)
        
else:
    print("Error: Invalid choice.")