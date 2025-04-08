

import java.util.*;

class EmpBonus {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] salary = new double[10];
        double[] bonus_Salary = new double[10];

        for (int i = 0; i < 10; i++) {
            System.out.println("Enter the Employe" + (i + 1) + "Salary");
            salary[i] = scanner.nextDouble();

            System.out.println("Enetr the Year of service:\n");
            int years = scanner.nextInt();

            double bonus;
            if (years < 5) {
                bonus = salary[i] * 0.05;
            } else if (years <= 10) {
                bonus = salary[i] * 0.10;
            } else {
                bonus = salary[i] * 0.15;
            }
            bonus_Salary[i] = bonus;

        }
        for (int i = 0; i < 10; i++) {
            System.out.printf("Employe %.2f got %d with bonus %.2f\n", i, salary[i], bonus_Salary[i]);
        }

        scanner.close();
    }

}