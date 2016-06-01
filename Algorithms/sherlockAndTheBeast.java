import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int T = scan.nextInt();
        long[] arrayCombinations = new long[10];
        
        for (int i = 0; i < T; i++) {
            int N = scan.nextInt();
            
            ArrayList<Integer> fives = new ArrayList<>();
            ArrayList<Integer> threes = new ArrayList<>();
            
            int numberFives = 0;
            
            while (numberFives <= N) {
                fives.add(numberFives);
                numberFives += 5;
            }

            int numberThrees = 0;
            
            while (numberThrees <= N) {
                threes.add(numberThrees);
                numberThrees += 3;
            }

            /* for (int j = 0; j < fives.size(); j++)
            {
                System.out.println(fives.get(j));
            }
            for (int j = 0; j < threes.size(); j++)
            {
                System.out.println(threes.get(j));
            } */
            // Logique
            
            long highest = 0;
            int numberOfMatches = 0;
            for (int j = 0; j < fives.size(); j++) {
                for (int k = 0; k < threes.size(); k++) {
                    if (fives.get(j) + threes.get(k) == N) {
                        //System.out.println(fives.get(j) + " " + threes.get(k));
                        numberOfMatches++;
                        String resultingNumber = "";
                        for (int l = 0; l < threes.get(k); l++) {
                            resultingNumber = resultingNumber + "5";
                        }
                        for (int l = 0; l < fives.get(j); l++) {
                            resultingNumber = resultingNumber + "3";
                        }
                        //System.out.println(resultingNumber);
                        long check = Long.parseLong(resultingNumber);
                        if (check > highest) {
                            highest = check;
                        }
                    }
                }
            }
            if (numberOfMatches == 0) {
                arrayCombinations[i] = -1;   
            } else {
                arrayCombinations[i] = highest;
            }
        }
        for (int i = 0; i < T; i++) {
            System.out.println(arrayCombinations[i]);
        }
    }
}