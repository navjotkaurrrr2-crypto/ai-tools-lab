#include <iostream>
using namespace std;

int binarySearch(int numbers[], int size, int target) {
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        int middle = (low + high) / 2;

        if (numbers[middle] == target) {
            return middle;
        } else if (numbers[middle] < target) {
            low = middle + 1;
        } else {
            high = middle - 1;
        }
    }

    return -1;
}

int main() {
    int numbers[] = {10, 20, 30, 40, 50};
    int target = 30;

    int size = sizeof(numbers) / sizeof(numbers[0]);

    int result = binarySearch(numbers, size, target);

    if (result != -1) {
        cout << "Element found at index: " << result << endl;
    } else {
        cout << "Element not found" << endl;
    }

    return 0;
}