# This program creates a tuple containing other tuples and accesses its elements.

# Creating a nested tuple
nested_tuple = ((1, 2, 3), ('a', 'b', 'c'), (True, False))

# Accessing elements from the outer tuple
print("Entire tuple:", nested_tuple)
print("First inner tuple:", nested_tuple[0])
print("Second inner tuple:", nested_tuple[1])
print("Third inner tuple:", nested_tuple[2])

# Accessing elements from inner tuples
print("Element from first inner tuple:", nested_tuple[0][1])  # 2
print("Element from second inner tuple:", nested_tuple[1][2])  # 'c'
print("Element from third inner tuple:", nested_tuple[2][0])  # True
