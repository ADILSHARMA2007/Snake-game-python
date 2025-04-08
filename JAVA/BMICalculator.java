import java.util.Scanner;

public class BMICalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the number of persons: ");
        int numberOfPersons = scanner.nextInt();
        
        double[] weights = new double[numberOfPersons];
        double[] heights = new double[numberOfPersons];
        double[] bmis = new double[numberOfPersons];
        String[] weightStatus = new String[numberOfPersons];

        for (int i = 0; i < numberOfPersons; i++) {
            System.out.print("Enter weight (in kg) for person " + (i + 1) + ": ");
            weights[i] = scanner.nextDouble();
            System.out.print("Enter height (in meters) for person " + (i + 1) + ": ");
            heights[i] = scanner.nextDouble(

            bmis[i] = weights[i] / (heights[i] * heights[i]);
 
            if (bmis[i] < 18.5) {
                weightStatus[i] = "Underweight";
            } else if (bmis[i] < 24.9) {
                weightStatus[i] = "Normal weight";
            } else if (bmis[i] < 29.9) {
                weightStatus[i] = "Overweight";
            } else {
                weightStatus[i] = "Obesity";
            }
        }


        System.out.printf("%-10s %-10s %-10s %-15s%n", "Height", "Weight", "BMI", "Weight Status");
        for (int i = 0; i < numberOfPersons; i++) {
            System.out.printf("%-10.2f %-10.2f %-10.2f %-15s%n", heights[i], weights[i], bmis[i], weightStatus[i]);
        }
        
        scanner.close();
    }
}
