using System;

public class Solution {
	// Add your code here
    public static void printArray <E> (E[] array) {
        foreach (E element in array) {
            Console.WriteLine(element);
        }
    }

    static void Main(string[] args) {
        int[] vInt = new int[] {1, 2, 3};
        string[] vString = new string[] {"Hello", "World"};
        
        printArray<int>(vInt);
        printArray<string>(vString);
    }
}