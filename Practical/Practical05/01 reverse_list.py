# This program reverses a list using different methods.

# Method 1: Using slicing
def reverse_with_slicing(lst):
    return lst[::-1]

# Method 2: Using reversed()
def reverse_with_reversed(lst):
    return list(reversed(lst))

# Method 3: Using a loop
def reverse_with_loop(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# Method 4: Using list.reverse()
def reverse_with_inplace(lst):
    lst.reverse()
    return lst

# Input list
numbers = [1, 2, 3, 4, 5]

print("Original List:", numbers)
print("Reversed (Slicing):", reverse_with_slicing(numbers))
print("Reversed (reversed() function):", reverse_with_reversed(numbers))
print("Reversed (Loop method):", reverse_with_loop(numbers))

# Demonstrating in-place reversal
numbers_copy = numbers[:]  # Copying original list
reverse_with_inplace(numbers_copy)
print("Reversed (In-place):", numbers_copy)
