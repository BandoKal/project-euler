# https://projecteuler.net/problem=5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple(n):
    """
    Returns the smallest positive number that is evenly divisible by all of the numbers from 1 to n.
    """
    i = n
    while True:
        for j in range(1, n+1):
            if i % j != 0:
                break
            if j == n:
                return i
        i += n

print(smallest_multiple(20))
