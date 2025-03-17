# This program demonstrates tuple unpacking and swapping values using tuple unpacking.

# Creating a tuple with three elements
my_tuple = (10, 20, 30)

# Tuple unpacking
a, b, c = my_tuple
print("Original Values:")
print(f"a = {a}, b = {b}, c = {c}")

# Swapping values using tuple unpacking
a, b, c = c, a, b # circular swap a -> b , b -> c , c -> a
print("After Swapping:")
print(f"a = {a}, b = {b}, c = {c}")
