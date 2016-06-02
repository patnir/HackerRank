#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void checkPrime(int number) {
    if (number == 1) {
        printf("Not prime\n");
        return;
    }
    int check = (int)sqrt(number);
    int i;
    for (i = 2; i <= check; i++) {
        if (number % i == 0) {
            printf("Not prime\n");
            return;
        }
    }
    printf("Prime\n");
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