# This program checks if a number is present in a nested list/tuple/set using a loop.

nested_data = [(1, 2, 3), [4, 5, 6], {7, 8, 9}]  # Mixed types
search_element = 7

# Using a loop to check membership
found = False  # Initialize flag

for group in nested_data:  # Iterate through each nested structure
    if search_element in group:  # Check if element is inside the current structure
        found = True
        break  # Exit the loop once found

print(f"Is {search_element} present? {found}")
