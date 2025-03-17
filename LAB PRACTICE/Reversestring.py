# Take input from the user
user_input = input("Enter a string: ")  

# Reverse the string and join characters with a comma
reversed_string = user_input[::-1]  # This reverses the string
result = ",".join(reversed_string)  # This adds a comma between each character

# Print the final result
print(result)