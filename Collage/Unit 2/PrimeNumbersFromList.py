# 8.Program to return prime numbers from a list

'''
Problem Statement
Write a program that takes a list of numbers as input and returns a new list containing only the prime numbers.

Input
A list of positive integers:

Each number N (1 ≤ N ≤ 10⁶).
Output
A list of prime numbers from the given input list.

Example 1
Input:
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]  
Output:
[2, 3, 5, 7]  
Explanation:
2, 3, 5, 7 are prime numbers.
4, 6, 8, 9, 10 are not prime.

Example 2
Input:
numbers = [11, 13, 17, 19, 23, 29, 31]  
Output:
[11, 13, 17, 19, 23, 29, 31]  
Explanation:
All numbers in the list are prime.

Constraints
✔ The input list contains at least one number.
✔ 1 is not a prime number (it has only one factor).
✔ The function should work efficiently for large numbers (up to 10⁶).


'''

numbers = list(map(int, input("Enter a list of numbers separated by space or comma: ").replace(",", " ").split()))

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

prime_numbers = [num for num in numbers if is_prime(num)]
print(prime_numbers)