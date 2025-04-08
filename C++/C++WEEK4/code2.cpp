#include <iostream>
#include <string>
using namespace std;

class Product
{
private:
    int productID;
    string productName;
    double price;
    int quantity;

public:
    Product(){
        productID = 0;
        productName = "Unknown";
        price = 0.0;
        quantity = 0;}
    Product(int id, string name, double p, int q)
    {
        productID = id;
        productName = name;
        price = p;
        quantity = q;}
    double calculateTotalPrice(){
        return price * quantity;}
    void displayProductInfo(){
        cout << "Product ID: " << productID << endl;
        cout << "Product Name: " << productName << endl;
        cout << "Price: $" << price << endl;
        cout << "Quantity: " << quantity << endl;
        cout << "Total Price: $" << calculateTotalPrice() << endl;
        cout << "-----------------------" << endl;}
    ~Product(){
        cout << "Product " << productName << " removed from the cart." << endl;}
};

void displayCart(Product cart[], int size){
    cout << "Shopping Cart Details:\n";
    for (int i = 0; i < size; i++){
        cart[i].displayProductInfo();}
}
int main(){
    Product cart[] = {
        Product(201, "Laptop", 899.99, 1),
        Product(202, "Smartphone", 499.50, 2),
        Product(203, "Headphones", 79.99, 3)};

    int cartSize = sizeof(cart) / sizeof(cart[0]);
    displayCart(cart, cartSize);

    return 0;
}
