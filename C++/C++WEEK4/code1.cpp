#include <iostream>
#include <string>
using namespace std;

class Book{
private:
    int bookID;
    string title;
    string author;
    double price;

public:
    Book(){
        bookID = 0;
        title = "Unknown";
        author = "Unknown";
        price = 0.0;}

    Book(int id, string t, string a, double p){
        bookID = id;
        title = t;
        author = a;
        price = p;}
    void displayBookInfo(){
        cout << "Book ID: " << bookID << endl;
        cout << "Title: " << title << endl;
        cout << "Author: " << author << endl;
        cout << "Price: $" << price << endl;
        cout << "-----------------------" << endl;}
};
int main()
{
    Book book1(101, "The Great Gatsby", "F. Scott Fitzgerald", 10.99);
    Book book2(102, "1984", "George Orwell", 8.99);
    Book book3(103, "To Kill a Mockingbird", "Harper Lee", 12.50);

    Book defaultBook;
    cout << "Library Book Details:\n";
    book1.displayBookInfo();
    book2.displayBookInfo();
    book3.displayBookInfo();
    defaultBook.displayBookInfo();

    return 0;
}
