# Project Euler ID #1
# Add all the natural numbers below one thousand
# that are multiples of 3 or 5

threes = 3*(1:floor(999/3))
fives = 5*(1:floor(999/5))
fifteens = 15*(1:floor(999/15))

answer = sum(threes,fives,(-1)*fifteens)
answer

