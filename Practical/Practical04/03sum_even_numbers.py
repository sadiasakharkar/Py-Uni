# This program calculates the sum of all even numbers from 1 to 100 using a for loop.

sum_even = sum(i for i in range(2, 101, 2))  # Sum of even numbers from 2 to 100
print(f"Sum of even numbers from 1 to 100: {sum_even}")
