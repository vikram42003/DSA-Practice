#include <iostream>
using namespace std;

// Calculator - Inline and friend functions
// Take two private data members
// - An Inline func to find the sum of the squares of the two numbers
// - A friend function to find out the sum of the two private data members
// Display results using standard io functions

class Calculator {
    private:
    int x;
    int y;

    public:
    friend int sum(Calculator);

    Calculator(int x, int y) {
        this->x = x;
        this->y = y;
    }

    inline int square() {
        return (x * x) + (y * y);
    }
};

int sum(Calculator c) {
    return c.x + c.y;
}

int main() {
    Calculator c = {2, 3};

    cout << c.square() << endl;

    cout << sum(c) << endl;
}