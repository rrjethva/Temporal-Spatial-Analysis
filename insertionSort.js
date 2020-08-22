// insertionSort.js
// Quick sort algorithm written in JavaScript with Temporal Analysis for 10,000 random array elements
// NCU.edu
// School of Business & Technology Managment
// TIM-6110
// Author: Ravi Jethva
// Date: August 23, 2020


const insertionSort = (array) => {
    // insertion sort algorithm
    for (let i = 1; i < array.length; i++) {
        let j = i - 1;
        let temp = array[i];
        while (j >= 0 && array[j] > temp) {
            array[j + 1] = array[j];
            j--;
        }
        array[j + 1] = temp
    }
    return array;
}

// set array length to 10,000 elements, random elements pushed into empty array
const arrayLength = 10000;
const array = [];
for (let i = 0; i < arrayLength; i++) {
    array.push(Math.floor(Math.random() * 10000) + 1)
}

// display insertion sorted array with temporal analysis
insertionSort(array);
console.time(array);
console.timeEnd(array);