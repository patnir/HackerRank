import java.io.*;
import java.util.*;

public class Solution {

    public static int DayFine = 15;
    public static int MonthFine = 500;
    public static int YearFine = 10000;
    
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int actualDay = scan.nextInt();
        int actualMonth = scan.nextInt();
        int actualYear = scan.nextInt();
        int expectedDay = scan.nextInt();
        int expectedMonth = scan.nextInt();
        int expectedYear = scan.nextInt();
        
        int diffDay = actualDay - expectedDay;
        int diffMonth = actualMonth - expectedMonth;
        int diffYear = actualYear - expectedYear;
        
        // System.out.println("" + diffDay + " " + diffMonth + " " + diffYear);
        
        if (diffYear > 0) {
            System.out.println(diffYear * YearFine);
        } 
        else if (diffMonth > 0) {
            System.out.println(diffMonth * MonthFine);
        }
        else if (diffDay > 0) {
            System.out.println(diffDay * DayFine);
        } else {
            System.out.println(0);
        }
    }
}