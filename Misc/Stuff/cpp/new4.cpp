#include <iostream>
#include <string>
using namespace std;

class Student {
    private:
    int marks[][];


};

int main() {
    int st, sb;

    cout << "Enter the number of students: ";
    cin >> st;
    cout << endl;

    cout << "Enter the number of subjects: ";
    cin >> sb;
    cout << endl;

    int marks[st][sb];

    for (int i = 0; i < st; i++) {
        cout << "Enter the marks for student " << i << ": " << endl;
        for (int j = 0; j < sb; j++) {
            cin >> marks[i][j];
        }
    }
}