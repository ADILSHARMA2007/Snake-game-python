#include <iostream>
using namespace std;

class Student
{
private:
    string studentID;
    string name;
    double marks[5];

public:
    Student(string id, string studentName, double studentMarks[5])
    {
        studentID = id;
        name = studentName;
        for (int i = 0; i < 5; i++){
            marks[i] = studentMarks[i];}
    }

    double calculateAverage(){
        double sum = 0;
        for (int i = 0; i < 5; i++){
            sum += marks[i];}
        return sum / 5;}
    void displayDetails(){
        cout << "Student ID: " << studentID << endl;
        cout << "Name: " << name << endl;
        cout << "Marks: ";
        for (int i = 0; i < 5; i++){
            cout << marks[i] << " ";}
        cout << endl;
        cout << "Average Marks: " << calculateAverage() << endl; }
};
int main(){
    double marks1[5] = {85, 90, 78, 88, 92};
    double marks2[5] = {76, 81, 69, 85, 80};

    Student student1("S001", "Aakash", marks1);
    Student student2("S002", "Krishna", marks2);

    cout << "Student Details:\n";
    student1.displayDetails();
    cout << endl;
    student2.displayDetails();

    return 0;
}