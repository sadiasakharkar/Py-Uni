def determineTriangle(a, b, c):
    
    if a + b <= c or b + c <= a or a + c <= b:
        return "Not a triangle"
    
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

result = determineTriangle(a, b, c)
print(result)