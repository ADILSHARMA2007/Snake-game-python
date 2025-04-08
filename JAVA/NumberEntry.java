import java.util.Scanner;

public class NumberEntry {
    public static void main(String[] args) {
        double[] numbers = new double[10];
        double total = 0.0;
        int index = 0;

        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Enter a number (0 or negative number to stop): ");
            double num = scanner.nextDouble();

            if (num <= 0 || index == 10) {
                break;}

            numbers[index] = num;
            index++;}

        System.out.print("Entered numbers: ");
        for (int i = 0; i < index; i++) {
            System.out.print(numbers[i] + " ");
            total += numbers[i];}

        System.out.println("\nTotal sum of the numbers: " + total);

        scanner.close();
    }
}
