# 6.Program to check whether a string is a palindrome or not

'''
Problem Statement
Write a program to check whether a given string is a palindrome or not. A palindrome is a string that reads the same forward and backward.

Input
A single string (consisting of letters, numbers, or symbols).
Output
"Palindrome" if the string is the same when reversed.
"Not a Palindrome" otherwise.

Example 1
Input: racecar
Output: Palindrome

Example 2
Input: hello
Output: Not a Palindrome

Example 3 (Case insensitive & spaces ignored)
Input: A man a plan a canal Panama
Output: Palindrome

'''

string = input("Enter a string: ")

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")