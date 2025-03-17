# This program concatenates two tuples and sorts the resulting tuple in ascending and descending order.

# Creating two tuples
tuple1 = (5, 2, 9, 1)
tuple2 = (8, 3, 7, 4)

# Concatenating tuples
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)

# Sorting in ascending order
sorted_asc = tuple(sorted(concatenated_tuple))
print("Sorted in Ascending Order:", sorted_asc)

# Sorting in descending order
sorted_desc = tuple(sorted(concatenated_tuple, reverse=True))
print("Sorted in Descending Order:", sorted_desc)
