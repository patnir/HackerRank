#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void mSort(float *array, int start, int end)
{
    
}

void merge(float *array, int start, int middle, int end) 
{
    
}

int main() {
    int i;
    fscanf(stdin, "%d", &i);
    int* array = (int *)malloc(sizeof(int) * i);
    int j;
    for (j = 0; j < i; j++) {
        fscanf(stdin, "%d", &array[j]);
    }
    mSort(array, 0, i - 1);
    return 0;
}