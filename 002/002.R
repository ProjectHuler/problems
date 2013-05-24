# Project Euler ID #2
# Each new term in the Fibonacci sequence is generated 
# by adding the previous two terms. By starting with 1 
# and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence 
# whose values do not exceed four million, find the sum 
# of the even-valued terms.

fib = c(1,2)
next_val = fib[ length(fib) - 1 ] + fib[ length(fib) ]

while ( next_val < 4000000 )
	{
	next_val = fib[ length(fib) - 1 ] + fib[ length(fib) ]
	if ( next_val < 4000000 )
		{
		fib = c(fib,next_val)
		}
	}

answer = sum( fib , (-1)*fib*(fib %% 2))
answer


