import java.util.*;

/**
 * Simple program that includes one class "SortedStack" which uses a scanner to read the
 * user's input. The user will be asked to enter a list of integers, which will keep going until
 * the user wants to be done. We are using the Collections Framework to store these numbers into
 * a stack, as well as sorting them from smallest to largest and making sure stack functions are
 * able to work correctly on this list.
 * 
 * @author James Zafiri
 * @version 1.0.0
 * @since Week 5 of CSC6031
 */
public class SortedStack {
    /**
     * This is our main method where we will interact with the user to obtain their
     * inputted integers. We will also store them into a stack and sort them using
     * a helper method and the Java Collections Framework.
     * @param args an array of numbers that will be inputed by the user one after another
     */
    public static void main(String[] args) {
        // scanner that will read the user's input
        Scanner scanner = new Scanner(System.in);

        // creates an empty stack to store integers
        Stack<Integer> stack = new Stack<>();

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

                // add the number to the stack
                pushSorted(stack, number);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid integer or 'done' to finish.");
            }
        }

        // prints the sorted stack for the user to see
        System.out.println("Sorted List of Integers:");
        while (!stack.isEmpty()) {
            System.out.print(stack.pop() + " ");
        }

        scanner.close();
    }

    /**
     * This is a helper method that we will use to enter an integer into the stack
     * while still keeping it sorted
     * @param stack an array of numbers that is our stack we are working with
     * @param number the number that is going to be added into the stack
     */
    private static void pushSorted(Stack<Integer> stack, int number) {
        // temporary stack that will be used to reorder the elements
        Stack<Integer> tempStack = new Stack<>();

        // as long as the stack is not empty and the number being entered is bigger than one on top of stack
        while (!stack.isEmpty() && stack.peek() < number) {
            // enters that top number to temporary stack
            tempStack.push(stack.pop());
        }

        // adding the inputted number to the stack after sorting temporary stack
        stack.push(number);

        // as long as the temporary stack is not empty, add the top element of it to the original stack
        while (!tempStack.isEmpty()) {
            stack.push(tempStack.pop());
        }
    }
}
