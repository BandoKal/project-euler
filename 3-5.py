# https://projecteuler.net/problem=1
# If we list all the natural numbers below that are multiples of or, we get and. The sum of these multiples is. Find the sum of all the multiples of or below.n = 1000
a = 3
b = 5
sum = 0
n = int(input("Enter a number: "))

for i in range(n):
    if i % a == 0 or i % b == 0:
        sum += i

print(sum)
