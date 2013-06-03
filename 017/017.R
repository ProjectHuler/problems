# Project Euler ID #17
# If all the numbers from 1 to 1000 (one thousand) 
# inclusive were written out in words, how many letters 
# would be used?

starttime = date()
answer = 0

ones = c( "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" )
for(i in 1:length(ones))
{
	ones[i] = length(strsplit(ones[i],"")[[1]])
}
ones = as.numeric(ones)

tweens = c( "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" )
for(i in 1:length(tweens))
{
	tweens[i] = length(strsplit(tweens[i],"")[[1]])
}
tweens = as.numeric(tweens)


tens = c("ten","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" )
for(i in 1:length(tens))
{
	tens[i] = length(strsplit(tens[i],"")[[1]])
}
tens = as.numeric(tens)


hundred = "hundred"
hundred = length(strsplit(hundred,"")[[1]])
thousand = "thousand"
thousand = length(strsplit(thousand,"")[[1]])

for( i in 1:1000 )
{
	if( log10(i) == 3 )
	{
		answer = answer + 3 + thousand
	}
	if( trunc(log10(i)) == 2 )
	{
		# 3 at the end is "and"
		answer = answer + ones[ floor(i/100) ] + hundred + 3
		if( i%%100 > 1 && i%%100 < 20 )
		{
			answer = answer + c(ones,tweens)[i%%100]
		}
		if( i%%100 >= 20 )
		{
			answer = answer + tens[ floor( (i%%100)/10 ) ]
			if( i%%10 > 0 )
			{
				answer = answer + ones[i%%10]
			}

		}
	}
	if( trunc(log10(i)) == 1 )
	{
		if( i%%100 > 1 && i%%100 < 20 )
		{
			answer = answer + c(ones,tweens)[i%%100]
		}
		if( i%%100 >= 20 )
		{
			answer = answer + tens[ floor( (i%%100)/10 ) ]
			if( i%%10 > 0 )
			{
				answer = answer + ones[i%%10]
			}
		}
	}
	if( trunc(log10(i)) == 0 )
	{
		answer = answer + ones[i]
	}
	print(c(i,answer))
	flush.console()
}

print(answer)
print(starttime)
print(date())

