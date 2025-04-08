import java.util.Scanner;

public class Bonus {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        double[] salaries = new double[10];
        double[] yearsOfService = new double[10];
        double[] bonuses = new double[10];
        double[] newSalaries = new double[10];
        
        double totalBonus = 0;
        double totalOldSalary = 0;
        double totalNewSalary = 0;

        for (int i = 0; i < 10; i++) {
            System.out.print("Enter salary for employee " + (i + 1) + ": ");
            while (true) {
                if (scanner.hasNextDouble()) {
                    salaries[i] = scanner.nextDouble();
                    break;
                } else {
                    System.out.print("Invalid input. Please enter a valid salary: ");
                    scanner.next(); 
                }
            }

            System.out.print("Enter years of service for employee " + (i + 1) + ": ");
            while (true) {
                if (scanner.hasNextDouble()) {
                    yearsOfService[i] = scanner.nextDouble();
                    break;
                } else {
                    System.out.print("Invalid input. Please enter valid years of service: ");
                    scanner.next();}}}

        for (int i = 0; i < 10; i++) {
            if (yearsOfService[i] > 5) {
                bonuses[i] = salaries[i] * 0.05;} 
            else {
                bonuses[i] = salaries[i] * 0.02;}
            newSalaries[i] = salaries[i] + bonuses[i];
            totalBonus += bonuses[i];
            totalOldSalary += salaries[i];
            totalNewSalary += newSalaries[i];}

        System.out.println("Total Bonus Payout: " + totalBonus);
        System.out.println("Total Old Salary: " + totalOldSalary);
        System.out.println("Total New Salary: " + totalNewSalary);
        
        scanner.close();
    }
}
