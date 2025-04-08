import java.util.Scanner;

public class MaxMinUsingArrays {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Ask the user how many numbers they want to enter
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();

        // Initialize the array to store the numbers
        int[] numbers = new int[n];

        // Input elements into the array
        for (int i = 0; i < n; i++) {
            System.out.print("Enter number " + (i + 1) + ": ");
            numbers[i] = scanner.nextInt();
        }

        // Initialize variables for maximum and minimum numbers
        int max = numbers[0];
        int min = numbers[0];
        int maxIndex = 0;
        int minIndex = 0;

        // Loop through the array to find the maximum and minimum values
        for (int i = 1; i < n; i++) {
            if (numbers[i] > max) {
                max = numbers[i];
                maxIndex = i; // Update the max index
            }
            if (numbers[i] < min) {
                min = numbers[i];
                minIndex = i; // Update the min index
            }
        }

        // Set the maximum value's index to 0
        numbers[maxIndex] = numbers[0];
        numbers[0] = max;

        // Set the minimum value's index to -1 (This is technically impossible,
        // but we can just print a message as it doesn't make sense to assign -1 to an
        // array index.)
        // Instead, we'll print the result as requested in the prompt.
        System.out.println("Maximum number index changed to 0.");
        System.out.println("Minimum number index set to -1 (not possible in array, so we print the result).");

        // Display the updated array
        System.out.print("Updated array: ");
        for (int num : numbers) {
            System.out.print(num + " ");
        }

        // Display the results
        System.out.println("\nMaximum number: " + max);
        System.out.println("Minimum number: " + min);

        scanner.close();
    }
}
