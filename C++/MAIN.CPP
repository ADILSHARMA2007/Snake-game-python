#include<iostream>

using namespace std;

class car{
    public:
    string brand;
    string model;
    int year;
    
    void details(){
        cout <<"the brand of the car is "<< brand << endl <<"The model of the car is " << model <<endl <<"the year of manufacturing is" << year <<endl;
    }
};

int main(){
    car Car1;
    Car1.brand = "TOYOTA";
    Car1.model = "INOVA";
    Car1.year = 2010;

    Car1.details();

    return 0;
}