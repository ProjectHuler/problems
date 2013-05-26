#include<stdio.h>

int solve002( int a, int b, int limit, int answer);

int main(void)
{
	int p1 = 1;
	int p2 = 2;
	int p3 = 4000000;
	int answer = 0;

	if( p1%2 == 0 )
	{ answer += p1;	}
	if( p2%2 == 0 )
	{ answer += p2;	}

	answer = solve002( p1,p2,p3,answer );
	printf("%i\n",answer);
}

int solve002( int a, int b, int limit, int sum )
{
	int c = a + b;
	if( c < limit )
	{
		sum = solve002( b,c,limit,sum );
		if( c%2 == 0 )
		{
			sum += c;
		}
	}
	return sum;
}

/**************

while method, no recursion	

int solve002( int a, int b, int limit, int sum )
{
	int c = a + b;
	while( c < limit )
	{
		if( c%2 == 0 )
		{
			sum += c;
		}
		a = b;
		b = c;
		c = a+b;
	}
	return sum;
}

**************/
