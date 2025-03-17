def is_prime(n):
    """Function to check if a number is prime"""
    if n < 2:
        return False
    i = 2
    while i * i <= n:  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False  # Not a prime number
        i += 1
    return True  # Prime number

def find_primes(a, b):
    """Function to find all prime numbers between a and b using a while loop"""
    primes = []
    num = a  # Start from a
    while num <= b:  # Continue until b
        if is_prime(num):
            primes.append(num)  # Add to the list if prime
        num += 1  # Increment number
    return primes

# Example usage
a = int(input("Enter the lower bound (a): "))
b = int(input("Enter the upper bound (b): "))
print("Prime numbers:", find_primes(a, b))
