# Set up a Fibonacci generator. This saves us from having to save an array of
# numbers.
def fibonacci():
    i_minus_2 = 1
    i_minus_1 = 2
    while 1:
        i = i_minus_2+i_minus_1
        i_minus_2 = i_minus_1
        i_minus_1 = i
        yield i

fib = fibonacci()
# Initiate the solution to an result of 2, since the Fibonacci series always
# starts at 1, followed by 2, and 2 is always even.
fib_sum = 2
while 1:
    # Grab the next Fibonacci number from the generator.
    next_fib = fib.next()
    if next_fib < 4000000:
        if next_fib%2:
            fib_sum += next_fib
    else:
        break

print fib_sum
