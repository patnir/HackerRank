#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void checkPrime(int number) {
    printf("%d\n", number);
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int T;
    scanf("%d", &T);
    while (T-- > 0) {
        int i;
        scanf("%d", &i);
        checkPrime(i);
    }
    return 0;
}