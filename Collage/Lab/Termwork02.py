# Python Operator Precedence and Associativity Demonstration

# Operator Precedence Table:
# () - Parentheses
# x[index], x[index:index] - Indexing and Slicing
# await x - Await
# ** - Exponentiation
# +x, -x, ~x - Unary Plus, Minus, Bitwise NOT
# *, @, /, //, % - Multiplication, Matrix, Division, Floor Division, Modulus
# +, - - Addition, Subtraction
# <<, >> - Bitwise Shift
# & - Bitwise AND
# ^ - Bitwise XOR
# | - Bitwise OR
# in, not in, is, is not, <, <=, >, >=, !=, == - Comparison, Membership, Identity
# not x - Logical NOT
# and - Logical AND
# or - Logical OR
# if-else - Conditional Expression
# lambda - Lambda Expression
# := - Walrus Operator


# 1. Parentheses - Highest precedence
# Parentheses override default precedence to ensure controlled execution order
result = (10 + 5) * 2  # Addition inside parentheses first, then multiplication
print("Parentheses: (10 + 5) * 2 =", result)

# 2. Indexing and slicing - Evaluated before arithmetic operations
lst = [10, 20, 30, 40, 50]
print("Indexing: lst[2] =", lst[2])  # Retrieves the 3rd element
print("Slicing: lst[1:4] =", lst[1:4])  # Retrieves elements from index 1 to 3

# 3. Exponentiation - Right-to-left associativity
exp_result = 2 ** 3 ** 2  # Evaluates as 2 ** (3 ** 2) = 2 ** 9 = 512
print("Exponentiation: 2 ** 3 ** 2 =", exp_result)

# 4. Unary operators (+, -, ~) - Evaluated before multiplication/division
a = 5
print("Unary Plus: +5 =", +a)
print("Unary Minus: -5 =", -a)
print("Bitwise NOT: ~5 =", ~a)  # Inverts all bits (two's complement)

# 5. Multiplication, Division, Floor Division, Modulus
b = 10
print("Multiplication: 10 * 2 =", b * 2)
print("Division: 10 / 3 =", b / 3)  # Float division
print("Floor Division: 10 // 3 =", b // 3)  # Discards decimal part
print("Modulus: 10 % 3 =", b % 3)  # Remainder of division

# 6. Addition and Subtraction - Lower precedence than multiplication
print("Addition: 10 + 5 =", b + 5)
print("Subtraction: 10 - 5 =", b - 5)

# 7. Bitwise Shift Operators - Shift bits left or right
print("Left Shift: 5 << 1 =", 5 << 1)  # Equivalent to 5 * 2^1 = 10
print("Right Shift: 5 >> 1 =", 5 >> 1)  # Equivalent to 5 / 2^1 = 2

# 8. Bitwise AND, XOR, OR
c = 6  # 0b0110
d = 3  # 0b0011
print("Bitwise AND: 6 & 3 =", c & d)  # 0b0010 = 2
print("Bitwise XOR: 6 ^ 3 =", c ^ d)  # 0b0101 = 5
print("Bitwise OR: 6 | 3 =", c | d)  # 0b0111 = 7

# 9. Membership and Identity Operators
e = [1, 2, 3, 4]
print("Membership Operator: 2 in [1, 2, 3, 4] =", 2 in e)
print("Identity Operator: e is e =", e is e)

# 10. Logical NOT, AND, OR - Evaluated in decreasing order
p = True
q = False
print("Logical NOT: not True =", not p)  # Negates True to False
print("Logical AND: True and False =", p and q)  # False (both need to be True)
print("Logical OR: True or False =", p or q)  # True (one True is enough)

# 11. If-Else Conditional Expression - Lower precedence than logical operators
num = 10
print("If-Else Expression: 10 if True else 5 =", num if True else 5)

# 12. Lambda Expression - Short function creation
square = lambda x: x ** 2
print("Lambda Expression: square(4) =", square(4))

# 13. Walrus Operator (:=) - Assigns value inside an expression
if (n := 100) > 50:
    print("Walrus Operator: n := 100, so n > 50 =", n)

# Demonstrating precedence change when a higher priority operator is applied
# Normally, + and * follow precedence, but parentheses override
expr1 = 5 + 3 * 2  # Multiplication first, then addition: 5 + 6 = 11
expr2 = (5 + 3) * 2  # Parentheses force addition first: 8 * 2 = 16
print("Without parentheses: 5 + 3 * 2 =", expr1)
print("With parentheses: (5 + 3) * 2 =", expr2)

# Demonstrating associativity
expr3 = 10 - 5 - 2  # Left to right: (10 - 5) - 2 = 3
expr4 = 10 - (5 - 2)  # Parentheses change order: 10 - 3 = 7
print("Left associativity: 10 - 5 - 2 =", expr3)
print("Modified order with parentheses: 10 - (5 - 2) =", expr4)

expr5 = 4 + 2 * 3 ** 2  # 2 ** 2 is evaluated first, then multiplication, then addition
expr6 = (4 + 2) * 3 ** 2  # Parentheses force addition first
expr7 = 4 + (2 * 3) ** 2  # Parentheses change multiplication priority
print("Without parentheses: 4 + 2 * 3 ** 2 =", expr5)
print("With parentheses (4 + 2) * 3 ** 2 =", expr6)
print("With different order: 4 + (2 * 3) ** 2 =", expr7)