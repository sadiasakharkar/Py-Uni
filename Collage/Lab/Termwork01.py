# Python Operators Demonstration 

# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operations:")
print(f"Addition ({a} + {b}):", a + b)
print(f"Subtraction ({a} - {b}):", a - b)
print(f"Multiplication ({a} * {b}):", a * b)
print(f"Division ({a} / {b}):", a / b)
print(f"Exponentiation ({a} ** {b}):", a ** b)
print(f"Modulus ({a} % {b}):", a % b)
print(f"Floor Division ({a} // {b}):", a // b)
print("\n")

# Assignment Operators
c = 5
print("Assignment Operations:")
c += 3
print("c += 3 ->", c)
c -= 2
print("c -= 2 ->", c)
c *= 4
print("c *= 4 ->", c)
c /= 2
print("c /= 2 ->", c)
c %= 3
print("c %= 3 ->", c)
c **= 2
print("c **= 2 ->", c)
c //= 2
print("c //= 2 ->", c)
print("\n")

# Relational (Comparison) Operators
x = 15
y = 10
print("Comparison Operations:")
print(f"Is {x} equal to {y}?", x == y)
print(f"Is {x} not equal to {y}?", x != y)
print(f"Is {x} greater than {y}?", x > y)
print(f"Is {x} less than {y}?", x < y)
print(f"Is {x} greater than or equal to {y}?", x >= y)
print(f"Is {x} less than or equal to {y}?", x <= y)
print("\n")

# Logical Operators
p = True
q = False
print("Logical Operations:")
print(f"{p} AND {q}:", p and q)
print(f"{p} OR {q}:", p or q)
print(f"NOT {p}:", not p)
print("\n")

# Bitwise Operators
m = 5  # 0b0101
n = 3  # 0b0011
print("Bitwise Operations:")
print(f"Bitwise AND ({m} & {n}):", m & n)  # 0b0001 -> 1
print(f"Bitwise OR ({m} | {n}):", m | n)   # 0b0111 -> 7
print(f"Bitwise XOR ({m} ^ {n}):", m ^ n)  # 0b0110 -> 6
print(f"Bitwise NOT (~{m}):", ~m) # -(5+1) -> -6
print(f"Left Shift ({m} << 1):", m << 1) # 0b1010 -> 10
print(f"Right Shift ({m} >> 1):", m >> 1) # 0b0010 -> 2
print("\n")

# Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("Identity Operations:")
print("list1 is list2:", list1 is list2)  # False (Different objects)
print("list1 is list3:", list1 is list3)  # True (Same object)
print("list1 is not list2:", list1 is not list2)  # True
print("\n")

# Membership Operators
demo_string = "Hello Python"
print("Membership Operations:")
print("'H' in demo_string:", 'H' in demo_string)
print("'z' not in demo_string:", 'z' not in demo_string)
print("\n")
