#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int result(int n, int k) {
    int i, j;
    int max = 0;
    for (i = 1; i <= n; i++) {
        for (j = i + 1; j <= n; j++) {
            int check = i & j;
            //printf("%d %d\n", i, j);
            if (check > max && check < k) {
                max = check;
            }
        }
    }
    return max;
}

int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        int n; 
        int k; 
        scanf("%d %d",&n,&k);
        int q = k & n;
        printf("%d\n", result(n, k));
    }
    return 0;
}