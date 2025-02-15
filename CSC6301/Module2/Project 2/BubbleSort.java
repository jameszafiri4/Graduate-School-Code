/**
 * Simple class that provides an implementation of the BubbleSort sorting algorithm
 * for sorting an array of integers in an ascending order.
 * @author James Zafiri
 * @version 1.0.0
 * @since Week 2 of CSC6031
 */
public class BubbleSort {
    /**
     * Sorts a given array of integers using the bubble sort algorithm.
     * @param arr the array of integers that will be sorted
     */
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;

        // initial loop through array
        for (int i = 0; i < n - 1; i++) {
            swapped = false;

            // second loop to compare integers in array
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // swapping positions above
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // if there were no swaps made, then the array is already sorted
            if (!swapped) {
                break;
            }
        }
    }
    /**
     * This method will print out the elements of an array
     * @param args the array given
     */
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    /**
     * Main method of the class to test the BubbleSort algorithm
     * @param args the array that is given
     */
    public static void main(String[] args) {
        int[] myArray = {2, 45, 37, 21, 31, 50, 29, 22, 67, 88, 56};

        System.out.println("Array before sorting:");
        printArray(myArray);

        bubbleSort(myArray);

        System.out.println("Array after sorting:");
        printArray(myArray);
    }
}