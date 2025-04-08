import java.util.Scanner;

/**
 * Calculates the maximum number of possible handshakes among a group of students
 * where each student shakes hands with every other student exactly once.
 */
public class HandshakesPossibilities {

    public static void main(String[] args) {
        int numberOfStudents = getNumberOfStudents();
        int handshakes = calculateHandshakes(numberOfStudents);
        displayHandshakes(handshakes);
    }

    /**
     * Gets the number of students from user input with validation
     * @return valid number of students (>= 2)
     */
    public static int getNumberOfStudents() {
        Scanner scanner = new Scanner(System.in);
        int students = 0;
        
        while (students < 2) {
            System.out.print("Enter the number of students (minimum 2): ");
            if (scanner.hasNextInt()) {
                students = scanner.nextInt();
                if (students < 2) {
                    System.out.println("Please enter at least 2 students.");
                }
            } else {
                System.out.println("Invalid input. Please enter a number.");
                scanner.next(); // clear invalid input
            }
        }
        scanner.close();
        return students;
    }

    /**
     * Calculates the number of possible handshakes using combination formula
     * @param n number of students
     * @return number of possible handshakes
     */
    public static int calculateHandshakes(int n) {
        return (n * (n - 1)) / 2;
    }

    /**
     * Displays the result to the user
     * @param handshakes number of handshakes to display
     */
    public static void displayHandshakes(int handshakes) {
        System.out.println("Maximum number of handshakes: " + handshakes);
    }
}
