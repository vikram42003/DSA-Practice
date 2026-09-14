#include <iostream>

// Binary search

int main() {
    int arr[] = { 1, 3, 6, 9, 10 };

    int l = 0;
    int r = 4;

    int target = 10;

    while (l <= r) {
        int mid = l + (r - l) / 2;
        
        if (arr[mid] == target) {
            cout << "Element found at idx " << mid << endl;
        } else if (arr[mid] < target) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
}