#include<stdio.h>

int solve002( int a, int b, int limit, int answer);

int main(void) {
	int p1 = 1;
	int p2 = 2;
	int p3 = 4000000;
    // Start off the answer at 2.
	int answer = 2;

    // Recursively call the function solve002 to generate the next entry in the
    // Fibonacci sequence
    answer = solve002( p1,p2,p3,answer );
	printf("%i\n",answer);
}

int solve002( int a, int b, int limit, int sum ) {
	int c = a + b;
	if( c < limit ) {
		sum = solve002( b,c,limit,sum );
        // Test for even-ness, and add to the answer if it is even.
		if( c%2 == 0 ) {
			sum += c;
		}
	}
	return sum;
}
