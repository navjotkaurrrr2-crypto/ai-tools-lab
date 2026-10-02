# Code Conversion Between Languages Using AI

## Objective

To use AI to convert a working Python binary search program into Java, C++, and JavaScript, test each version, and evaluate whether the original logic was preserved.

## Original Python Program

```python
def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        middle = (low + high) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


numbers = [10, 20, 30, 40, 50]
target = 30

result = binary_search(numbers, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")