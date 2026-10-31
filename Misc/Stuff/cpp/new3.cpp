#include <iostream>
#include <string>
using namespace std;

// WAP to count total chars in a string

int main() {
    string str;
    getline(cin, str);

    int length = 0;

    for (int i = 0; str[i] != '\0'; i++) {
        length += 1;
    }

    std::cout << "Length: " << length << endl;

    return 0;
}