import java.util.Scanner;

public class ReverseNumber {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        
        // Convert number to digits
        int maxDigit = 10;
        int[] digits = new int[maxDigit];
        int index = 0;

        while (number > 0) {
            if (index == maxDigit) {
                // Increase the size of the array
                maxDigit += 10;
                int[] temp = new int[maxDigit];
                System.arraycopy(digits, 0, temp, 0, digits.length);
                digits = temp;
            }
            digits[index++] = number % 10;
            number /= 10;
        }

        // Display the digits in reverse order
        System.out.print("Reversed number: ");
        for (int i = index - 1; i >= 0; i--) {
            System.out.print(digits[i]);
        }
        System.out.println();
        
        scanner.close();
    }
}
