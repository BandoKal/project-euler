# https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

n = 100

# Calculate the sum of the squares of the first n natural numbers
sum_of_squares = sum(i**2 for i in range(1, n+1))

# Calculate the square of the sum of the first n natural numbers
square_of_sum = sum(range(1, n+1))**2

# Calculate the difference between the sum of the squares and the square of the sum
difference = square_of_sum - sum_of_squares

print(difference)


