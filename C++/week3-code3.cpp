#include <iostream>
using namespace std;

class BankAccount
{
private:
    string accountNumber;
    string accountHolderName;
    double balance;

public:
    BankAccount(string accNum, string accHolder, double bal = 0.0){
        accountNumber = accNum;
        accountHolderName = accHolder;
        balance = bal;}

    void deposit(double amount){
        if (amount > 0){
            balance += amount;
            cout << "Deposited $" << amount << ". New balance: $" << balance << endl;}
        else{
            cout << "Deposit amount must be positive." << endl;}
    }

    void withdraw(double amount){
        if (amount > 0 && amount <= balance){
            balance -= amount;
            cout << "Withdrew $" << amount << ". New balance: $" << balance << endl;}
        else{
            cout << "Insufficient funds or invalid amount." << endl;}
    }

    void display()
    {
        cout << "Account Number: " << accountNumber << endl;
        cout << "Account Holder: " << accountHolderName << endl;
        cout << "Balance: $" << balance << endl;
    }
};

int main(){
    BankAccount account("123456", "John Doe", 500.0);
    account.display();
    cout << endl;

    account.deposit(200);
    account.withdraw(100);
    account.withdraw(700); // Should print an insufficient funds message
    cout << endl;
    account.display();

    return 0;
}
