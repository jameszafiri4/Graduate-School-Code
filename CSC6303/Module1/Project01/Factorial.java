/**
 * Simple class that provides an implementation of a function
 * that will calculate the factorial of an integer.
 * This code is written in Java and was tested on Visual Studio Code.
 * @author James Zafiri
 * @version 1.0.0
 * @since Week 1 of CSC6303
 */

import java.util.Scanner;

public class Factorial {
    /**
     * Main method of the class to test the Factorial method
     * @param args the command line argument being passed
     */    
    public static void main(String[] args) {
        // calling fact() method to calculate the factorial
        fact();
    }

    /**
     * This is the method that will actually calculate the factorial
     * of the given number
     */ 
    public static void fact() {
        // scanner object being created for user input
        Scanner scanner = new Scanner(System.in);

        // asking user for a positive int
        System.out.print("Enter a positive integer: ");
        int n = scanner.nextInt();

        // making sure that the input actually is a positive int
        while (n < 0) {
            System.out.print("Sorry, only positive numbers, enter again: ");
            n = scanner.nextInt();
        }

        // based on the user input, calculate the factorial
        if (n == 0) {
            System.out.println("The factorial of 0 is 1");
        } else {
            int f = 1;
            for (int i = 1; i <= n; i++) {
                f *= i;
            }
            System.out.println("The factorial of " + n + " is " + f);
        }

        scanner.close();
    }
}
