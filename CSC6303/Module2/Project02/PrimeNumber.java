/**
 * Simple class that states whether or not a number is prime.
 * The program will keep asking for numbers until the user exits.
 * This code is written in Java and was tested on Visual Studio Code.
 * @author James Zafiri
 * @version 1.0.0
 * @since Week 2 of CSC6303
 */

import java.util.Scanner;

public class PrimeNumber {
    /**
     * Method to test if a number is prime
     * @param int the number that is being passed in to check if prime
     */   
    static boolean isPrime(int n) {
        // we know that both 0 and 1 are not prime
        if (n <= 1) return false;
        // we know that both 2 and 3 are prime
        if (n <= 3) return true;
        // first to check divisibility by 2 or 3
        if (n % 2 == 0 || n % 3 == 0) return false;
        // looking through potential divisors of n to check if prime
        for (int i = 5; i * i <= n; i += 6) {
            // checking divisibility of current divisor
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        // if there are no divisors found, it is a prime number
        return true;
    }

    /**
     * Main method of the class to ask the user for numbers
     * and check if they are prime
     * @param args the command line argument being passed
     */    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int number;
        // repeatedly asking user for numbers to check if they are prime
        do {
            System.out.print("Enter a positive number (0 or negative to exit): ");
            number = scanner.nextInt();

            // exit the loop if 0 or negative number is given
            if (number <= 0) {
                break;
            }

            // using method to check if number is prime and report to user
            if (isPrime(number)) {
                System.out.println(number + " is a prime number.");
            } else {
                System.out.println(number + " is not a prime number.");
            }

        } while (true);

        scanner.close();
    }
}
