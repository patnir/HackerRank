import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int[] array = new int[a];
        for (int i = 0; i < a; i++) {
            array[i] = s.nextInt();
        }
        int swaps = 0;
        boolean sorted = true;
        while (sorted) {
            sorted = false;
            for (int i = 0; i < a - 1; i++) {
                if (array[i] > array[i + 1]) {
                    int temp = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = temp; 
                    swaps++;
                    sorted = true;
                }
            }
        }
        System.out.printf("Array is sorted in %d swaps.\n", swaps);
        System.out.printf("First Element: %d\n", array[0]);
        System.out.printf("Last Element: %d\n", array[a - 1]);
    }
}