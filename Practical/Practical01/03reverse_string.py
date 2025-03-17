# This code reverses a user-input string and prints characters separated by commas

user_string = input("Enter a string: ")  # Taking user input
reversed_string = ",".join(reversed(user_string))  # Reversing and joining with commas
print(reversed_string)  # Printing the result
