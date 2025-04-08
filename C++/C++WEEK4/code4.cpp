#include <iostream>
#include <string>
using namespace std;

class Employee
{
private:
    int empID;
    string name;
    double salary;
    string designation;

public:
    // Parameterized constructor
    Employee(int id, string n, double s, string d) : empID(id), name(n), salary(s), designation(d) {}

    // Copy constructor
    Employee(const Employee &e)
    {
        empID = e.empID;
        name = e.name;
        salary = e.salary;
        designation = e.designation;
    }

    // Method to display employee details
    void displayDetails()
    {
        cout << "Employee ID: " << empID << endl;
        cout << "Name: " << name << endl;
        cout << "Salary: $" << salary << endl;
        cout << "Designation: " << designation << endl;
        cout << "-----------------------" << endl;
    }
};

int main()
{
    Employee E1(101, "Alice Johnson", 75000, "Software Engineer");
    Employee E2 = E1; // Using copy constructor

    cout << "Details of Employee E1:" << endl;
    E1.displayDetails();

    cout << "Details of Employee E2 (copy of E1):" << endl;
    E2.displayDetails();

    return 0;
}
