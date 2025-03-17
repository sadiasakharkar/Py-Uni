# This program finds the maximum and minimum elements in a list.

def find_min_max(lst):
    # Using inbuilt functions
    min_value = min(lst)
    max_value = max(lst)
    
    return min_value, max_value

# Input list
numbers = [3, 7, 1, 9, 2, 8, 6]

# Finding min and max
minimum, maximum = find_min_max(numbers)

print(f"List: {numbers}")
print(f"Minimum element: {minimum}")
print(f"Maximum element: {maximum}")
