# This program calculates the bonus for an employee based on experience and performance.

# Taking inputs
salary = int(input("Enter employee salary: "))
years_of_experience = int(input("Enter years of experience: "))
performance_rating = float(input("Enter performance rating (1 to 5): "))

# Initialize bonus percentage
bonus_percentage = 0

# Check performance rating first
if performance_rating < 3:
    print("No bonus due to low performance rating.")
else:
    # Determine bonus based on experience
    if years_of_experience > 10:
        bonus_percentage = 20
    elif years_of_experience >= 5:
        bonus_percentage = 10
    else:
        bonus_percentage = 5

    # Calculate bonus amount
    bonus_amount = (bonus_percentage / 100) * salary
    final_salary = salary + bonus_amount

    # Print results
    print(f"Bonus amount: {bonus_amount}")
    print(f"Final salary after bonus: {final_salary}")
