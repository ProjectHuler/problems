#include <stdio.h>

int main(void) {
    int sum=0;
    // Loop through integers 1 to 999 looking for integers that are divisible
    // by 3 or 5. If they are, then add to the running sum.
    for(int i=1; i<1000; i++) {
        if(i%3 == 0) {
            sum += i;
        }
        else if(i%5 == 0) {
            sum += i;
        }
    }
    printf("%i\n", sum);
    return 0;
}
