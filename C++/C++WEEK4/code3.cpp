#include <iostream>
#include <string>
using namespace std;

class MovieTicket
{
private:
    string movieName;
    int seatNumber;
    double price;
    bool isBooked;

public:
    // Constructor
    MovieTicket(string name, int seat, double p) : movieName(name), seatNumber(seat), price(p), isBooked(false) {}

    // Method to book the ticket
    void bookTicket()
    {
        if (!isBooked)
        {
            isBooked = true;
            cout << "Ticket booked for " << movieName << " at seat number " << seatNumber << " for $" << price << endl;
        }
        else
        {
            cout << "Ticket is already booked!" << endl;
        }
    }

    // Method to cancel the ticket
    void cancelTicket()
    {
        if (isBooked)
        {
            isBooked = false;
            cout << "Ticket for " << movieName << " at seat number " << seatNumber << " has been canceled." << endl;
        }
        else
        {
            cout << "No booking found to cancel!" << endl;
        }
    }

    // Method to display ticket details
    void displayTicketDetails()
    {
        cout << "Movie: " << movieName << endl;
        cout << "Seat Number: " << seatNumber << endl;
        cout << "Price: $" << price << endl;
        cout << "Status: " << (isBooked ? "Booked" : "Available") << endl;
    }

    // Destructor
    ~MovieTicket()
    {
        cout << "Ticket for " << movieName << " at seat number " << seatNumber << " is being deleted." << endl;
    }
};

int main()
{
    MovieTicket ticket1("Inception", 5, 12.50);
    MovieTicket ticket2("The Matrix", 10, 15.00);

    ticket1.displayTicketDetails();
    ticket1.bookTicket();
    ticket1.displayTicketDetails();
    ticket1.cancelTicket();
    ticket1.displayTicketDetails();

    ticket2.displayTicketDetails();
    ticket2.bookTicket();
    ticket2.displayTicketDetails();

    return 0;
}
