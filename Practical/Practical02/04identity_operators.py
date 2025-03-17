# This program compares objects using identity operators.

a = [1, 2, 3]  # List
b = a  # b references the same object as a
c = [1, 2, 3]  # A new list with the same content

print(f"a is b: {a is b}")  # True (same object)
print(f"a is c: {a is c}")  # False (different objects)

# Modify one object
b.append(4)
print(f"After modification, a: {a}")
print(f"After modification, b: {b}")
print(f"c remains unchanged: {c}")

print(f"a is b now: {a is b}")  # True (still same object)
print(f"a is c now: {a is c}")  # False (still different)
