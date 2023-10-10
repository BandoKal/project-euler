# https://projecteuler.net/problem=7
# What is the 10001st prime number?

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_nth_prime(n):
    """Find the nth prime number."""
    count = 0 # number of primes found
    number = 1 # the current number to check
    while count < n:
        number += 1
        if is_prime(number):
            count += 1
    return number

# Get the 10,001st prime
prime_10001 = find_nth_prime(10001)
print(f"The 10,001st prime number is: {prime_10001}")
