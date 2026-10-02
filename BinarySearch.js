function binarySearch(numbers, target) {
    let low = 0;
    let high = numbers.length - 1;

    while (low <= high) {
        let middle = Math.floor((low + high) / 2);

        if (numbers[middle] === target) {
            return middle;
        } else if (numbers[middle] < target) {
            low = middle + 1;
        } else {
            high = middle - 1;
        }
    }

    return -1;
}

const numbers = [10, 20, 30, 40, 50];
const target = 30;

const result = binarySearch(numbers, target);

if (result !== -1) {
    console.log("Element found at index:", result);
} else {
    console.log("Element not found");
}