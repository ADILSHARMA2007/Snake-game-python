#include <iostream>
using namespace std;

class Product
{
private:
    string productID;
    string productName;
    double price;
    int quantity;

public:
    Product(string id, string name, double p, int q){
        productID = id;
        productName = name;
        price = p;
        quantity = q;}

    double calculateTotalPrice(){
        return price * quantity;}

    void productDetails()
    {
        cout << "Product ID: " << productID << endl;
        cout << "Product Name: " << productName << endl;
        cout << "Price: Rs " << price << endl;
        cout << "Quantity: " << quantity << endl;
        cout << "Total Price: Rs " << calculateTotalPrice() << endl;
    }
};

void displayCart(Product products[], int size){
    cout << "Shopping Cart Details:\n";
    for (int i = 0; i < size; i++){
        products[i].productDetails();
        cout << endl;}
}

int main(){
    Product products[] = {
        Product("P001", "Laptop", 1200.50, 1),
        Product("P002", "Smartphone", 799.99, 2),
        Product("P003", "Headphones", 199.99, 3)};

    int size = sizeof(products) / sizeof(products[0]);
    displayCart(products, size);

    return 0;
}
