#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_SIZE = 100; // Maximum size of the array
int marks[MAX_SIZE];       // Array to hold marks
int currentSize = 0;      // Current number of students

void enterMarks(int n) {
    currentSize = n; // Set the current size to the number of students
    for (int i = 0; i < n; i++) {
        cout << "Enter marks for student " << (i + 1) << ": ";
        cin >> marks[i];
    }
}

float calculateAverage() {
    if (currentSize == 0) return 0; // Avoid division by zero
    float sum = 0;
    for (int i = 0; i < currentSize; i++) {
        sum += marks[i];
    }
    return sum / currentSize;
}

void findHighestLowest() {
    if (currentSize == 0) {
        cout << "No marks available." << endl;
        return;
    }
    int highest = marks[0];
    int lowest = marks[0];
    for (int i = 1; i < currentSize; i++) {
        if (marks[i] > highest) highest = marks[i];
        if (marks[i] < lowest) lowest = marks[i];
    }
    cout << "Highest marks: " << highest << endl;
    cout << "Lowest marks: " << lowest << endl;
}

int main() {
    int choice, n;

    do {
        cout << "\nMenu:" << endl;
        cout << "1. Enter marks of N students" << endl;
        cout << "2. Calculate average marks" << endl;
        cout << "3. Find highest and lowest marks" << endl;
        cout << "4. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter number of students: ";
                cin >> n;
                enterMarks(n);
                break;
            case 2:
                cout << "Average marks: " << calculateAverage() << endl;
                break;
            case 3:
                findHighestLowest();
                break;
            case 4:
                cout << "Exiting the program." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 4);

    return 0;
}
