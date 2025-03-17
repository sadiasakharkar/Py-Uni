# 7.Program to check whether a number is palindrome or not

'''
Problem Statement
Write a program to check whether a given number is a palindrome or not.

Input
A single positive integer N (1 ≤ N ≤ 10⁶).

Output
Print "Palindrome" if the number reads the same forward and backward. Otherwise, print "Not a Palindrome".

Example 1
Input:
N = 121
Output:
Palindrome
Explanation:
Reversing 121 gives 121, so it is a palindrome.

Example 2
Input:
N = 123
Output:
Not a Palindrome
Explanation:
Reversing 123 gives 321, so it is not a palindrome.

Constraints
✔ N is a positive integer (between 1 and 1,000,000).
✔ Output should be case-sensitive → "Palindrome" / "Not a Palindrome"
'''

number = input("Enter a number: ")

def is_palindrome(number):
    if  number == number[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

print(is_palindrome(number))