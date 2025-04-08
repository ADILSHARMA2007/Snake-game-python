public class ArmstrongNumber {
    public static void main(String[] args) {
        int number = 153; // You can change this number to test other values
        int originalNumber = number;
        int remainder;
        int result = 0;
        int digits = String.valueOf(number).length();

        while (number != 0) {
            remainder = number % 10;
            result += Math.pow(remainder, digits);
            number /= 10;
        }

        if (result == originalNumber) {
            System.out.println(originalNumber + " is an Armstrong number.");
        } else {
            System.out.println(originalNumber + " is not an Armstrong number.");
        }
    }
}
