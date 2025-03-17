# This program determines if a given year is a leap year with extra conditions for the 21st century.

# Taking input
year = int(input("Enter a year: "))

# Check leap year conditions
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Determine century category
if 2001 <= year <= 2100:
    if is_leap:
        print(f"{year} is a 21st Century Leap Year.")
    else:
        print(f"{year} is NOT a 21st Century Leap Year.")
else:
    if is_leap:
        print(f"{year} is a Leap Year.")
    else:
        print(f"{year} is NOT a Leap Year.")
