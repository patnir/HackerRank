import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        int[] arr = new int[t];
        for(int i = 0; i < t; i++){
            arr[i] = in.nextInt();
        }
        for (int i = 0; i < arr.length; i++) {
            int test = arr[i];
            int trust = 0;
            String result = "";
            for (int j = 0; j < test; j++) {
                result += "5";
            }
            int fives = test;
            int threes = 0;
            for (int j = test - 1; j >= 0; j-= 5) {
                if (fives % 3 == 0 && threes % 5 == 0) {
                    trust++;
                    break;
                } else {
                    if (test >= 5) {
                    String check = result.substring(0, j - 4) + "33333" + result.substring(j + 1, result.length());
                    result = check;
                    threes += 5;
                    fives -= 5;
                    } else {
                        break;
                    }
                }
            }
            if (fives % 3 == 0 && threes % 5 == 0) {
                    trust++;
                    System.out.println(result);
            } else {
                System.out.println(-1);
            }
        }
    }
}
