import java.util.*;

/**
 * Simple program that includes one class "SortedLinkedList" which uses a scanner to read the
 * user's input. The user will be asked to enter a list of integers, which will keep going until
 * the user wants to be done. We are using the Collections Framework to store these numbers into
 * a linked list, as well as sorting them from smallest to largest.
 * 
 * @author James Zafiri
 * @version 1.0.0
 * @since Week 4 of CSC6031
 */
public class SortedLinkedList {
    /**
     * This is our main method where we will interact with the user to obtain their
     * inputted integers. We will also store them into a linked list and sort them using
     * the Java Collections Framework.
     * @param args an array of numbers that will be inputed by the user one after another
     */
    public static void main(String[] args) {
        // scanner that will read the user's input
        Scanner scanner = new Scanner(System.in);

        // creates an empty linked list to store integers
        LinkedList<Integer> linkedList = new LinkedList<>();

        System.out.println("Enter a list of integers, pressing enter after each (type 'done' to finish):");

        // read the inputs until the user enters "done"
        while (true) {
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("done")) {
                break; // exits the loop once the user says they are done entering numbers
            }

            try {
                // turn the input into an integer
                int number = Integer.parseInt(input);

                // add the number to the linked list
                linkedList.add(number);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid integer or 'done' to finish.");
            }
        }

        // sorts the linked list from smallest to largest
        Collections.sort(linkedList);

        // prints the sorted linked list for the user to see
        System.out.println("Sorted List of Integers:");
        for (Integer number : linkedList) {
            System.out.print(number + " ");
        }

        scanner.close();
    }
}
