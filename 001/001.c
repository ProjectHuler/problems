/***************
Problem 001
Find the sum of all the multiples of 3 or 5 below 1000.
***************/

#include<stdio.h>
#include<math.h>

int solve001( int a, int b, int limit );

void main()
{
    int p1 = 3;
	int p2 = 5;
	int p3 = 1000;
	int ans = solve001(p1, p2, p3-1);
	printf("answer=%i\n",ans);
}

int solve001( int a, int b, int limit )
{
	/**********
	Method:	(3,6,9...999) + (5,10,15...995) - (15,30,45...)
	Separated into three lines for readability:
	(3+6+9+...+999) = 3(1+2+3...333) = 3(1+333)(333/2)
	**********/
	int solve001=0;
	solve001 += a*(1+floor(((float)limit)/a))*floor(((float)limit)/a)/2;
	solve001 += b*(1+floor(((float)limit)/b))*floor(((float)limit)/b)/2;
	solve001 -= (a*b)*(1+floor(((float)limit)/(a*b)))*floor(((float)limit)/(a*b))/2;
	return solve001;
}
