def find_max(*numbers):
    if not numbers:
        return "No numbers provided"
    return max(numbers)

# Taking user input
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Finding the maximum number
print("Maximum number:", find_max(*numbers))
