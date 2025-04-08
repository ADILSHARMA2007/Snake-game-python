#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    cout << right << setw(10) << fixed << setprecision(3) << 45.6789 << endl;

    cout << scientific << setprecision(6) << 0.00034567 << endl;
    cout << hex << uppercase << 255 << endl;

    cout << fixed << setprecision(4) << 987.654321 << endl;
    cout << scientific << setprecision(4) << -123.456 << endl;
    return 0;
}
