# Step 1: Define the nested structure
nested_data = [(1, 2, 3), [4, 5, 6], {7, 8, 9}]

# Step 2: Take user input for the element to search
element = int(input("Enter the number to search: "))

# Step 3: Check for membership using a loop
found = False
for sub_structure in nested_data:
    if element in sub_structure:  # Check if the element is in the current sublist/tuple/set
        found = True
        break  # Exit loop if found

# Step 4: Display result
if found:
    print(f"{element} is present in the nested structure.")
else:
    print(f"{element} is NOT present in the nested structure.")
