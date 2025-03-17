# This program converts decimal numbers to binary, performs bitwise operations, and checks logical conditions.

# Convert decimal to binary
num1 = int(input("Enter first decimal number: "))
num2 = int(input("Enter second decimal number: "))

binary1 = bin(num1)[2:]  # Convert to binary without '0b' prefix
binary2 = bin(num2)[2:]

print(f"Binary of {num1}: {binary1}")
print(f"Binary of {num2}: {binary2}")

# Perform bitwise operations
bitwise_and = num1 & num2
bitwise_or = num1 | num2
bitwise_xor = num1 ^ num2
bitwise_not1 = ~num1
bitwise_not2 = ~num2

print(f"Bitwise AND: {bin(bitwise_and)[2:]}")
print(f"Bitwise OR: {bin(bitwise_or)[2:]}")
print(f"Bitwise XOR: {bin(bitwise_xor)[2:]}")
print(f"Bitwise NOT of {num1}: {bin(bitwise_not1)}")
print(f"Bitwise NOT of {num2}: {bin(bitwise_not2)}")

# Logical operations
print(f"AND result > OR result: {bitwise_and > bitwise_or}")
print(f"XOR result is nonzero: {bitwise_xor != 0}")
