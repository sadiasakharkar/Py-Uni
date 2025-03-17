# 4. Program to Generate Student's Result Based on Marks
'''
Problem Statement

Write a program that accepts marks of five subjects and calculates the percentage. Based on the percentage, determine the student's result according to the following grading criteria:

Percentage (%)	Division
>= 75	First class with distinction
>= 60 and < 75	First class
>= 45 and < 60	Second class
>= 40 and < 45	Pass
< 40	Fail
Input

Five integer or floating-point numbers representing the marks in each subject.
0 ≤ marks ≤ 100 for each subject.
Output

The percentage (formatted up to 2 decimal places).
The result classification based on the given conditions.
Examples
Example 1

Input:

Marks: 85, 78, 92, 88, 76
Calculation:

Total Marks = 85 + 78 + 92 + 88 + 76 = 419
Percentage = (419 / 500) * 100 = 83.80%
Output:

Percentage: 83.80%
Result: First class with distinction
Example 2

Input:

Marks: 58, 62, 49, 55, 60
Calculation:

Total Marks = 58 + 62 + 49 + 55 + 60 = 284
Percentage = (284 / 500) * 100 = 56.80%
Output:

Percentage: 56.80%
Result: Second class
Example 3

Input:

Marks: 32, 45, 38, 40, 39
Calculation:

Total Marks = 32 + 45 + 38 + 40 + 39 = 194
Percentage = (194 / 500) * 100 = 38.80%
Output:

Percentage: 38.80%
Result: Fail
Constraints
Marks for each subject must be between 0 and 100.
The program should handle floating-point values for accurate calculations.
Ensure proper formatting of percentage (e.g., two decimal places).
'''


marks = [float(input(f"Enter marks for subject {i+1} :")) for i in range (5)]

total = sum(marks)
percentage = (total / 500) * 100

if percentage >= 75:
    result = "First class with distinction"
elif percentage >= 60 and percentage < 75:  
    result = "First class"
elif percentage >= 45 and percentage < 60:
    result = "Second class"
elif percentage >= 40 and percentage < 45:
    result = "Pass"
else:
    result = "Fail"
    
print(f"Percentage: {percentage:.2f}%")
print(f"Result: {result}")