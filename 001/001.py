"""
Project Euler Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
# List comprehention should be faster than Python for-loop.
# range(1,1000) returns a list from 1 to 999.
print sum([i for i in range(1,1000) if (i%3==0 or i%5==0)])
