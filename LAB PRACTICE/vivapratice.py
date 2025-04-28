# Nested loop to print multiplication table
# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f"{i} x {j} = {i * j}")
#     print()

# List basics
my_list = [1, 2, 3, 4, 5]

print(my_list[0])       # First element
print(len(my_list))     # Length of list
print(my_list[-1])      # Last element

# Tuple to list conversion
tuple_data = (1, 2, 3, 4, 5)
print(list(tuple_data))

# Creating and modifying lists
empty_list = []
list_constructor = list((3, 4, 5, 6))  # Fixed variable name typo

# Adding elements to list
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)
print(empty_list)

print(empty_list[1])     # Accessing second element
print(empty_list)

# Looping through list
for i in empty_list:
    print(i)

# Updating first element
empty_list[0] = 10

# Adding multiple elements
empty_list.append(4)
empty_list.extend([5, 6, 7])
print(empty_list)

# Inserting at specific position
empty_list.insert(2, "sadia")

# Updating multiple elements (using slicing)
empty_list[1:4] = ["sadia", "lavesh", "zikra"]

# Removing elements
del empty_list[-1]    # Delete last element
empty_list.pop()      # Pop last element
empty_list.remove("sadia")  # Remove element by value

# Deleting entire list
del empty_list

# Tuple and list operations
tuplee = (1, 2, 3, 4, 5)
print(type(tuplee))    # Checking type of tuple

t_to_l = list(tuplee)
print(type(t_to_l))    # Checking type after converting to list

# String operations
str_data = "Sadia Sakharkar"  # Renamed from str (str is a built-in type, better not to override)
print(type(str_data))         # Checking type of string

s_to_l = list(str_data)
print(type(s_to_l))            # Checking type after converting string to list
print(s_to_l)                  # Printing list of characters
