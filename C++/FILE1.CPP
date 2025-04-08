#include <iostream>
using namespace std;
int main(){
    int num1, num2;
    cout << "Enter two integers: ";
    cin >> num1 >> num2;
    int product = num1 * num2;

    int digitCount = (product == 0) ? 1 : 0;
    int temp = product;

    while (temp != 0){
        temp /= 10;
        digitCount++;}

    cout << "Product: " << product << endl;
    cout << "Digit Count: " << digitCount << endl;

    return 0;
    }
    