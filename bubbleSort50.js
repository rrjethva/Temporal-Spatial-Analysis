// bubbleSort50.js
// Bubble sort algorithm written in JavaScript with Temporal Analysis for 50 random array elements
// NCU.edu
// School of Business & Technology Managment
// TIM-6110
// Author: Ravi Jethva
// Date: August 23, 2020

function bubbleSort(array) {
    let n = array.length;
// bubble sort algorithm
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (array[j] > array[j + 1]) {
                let t = array[j];
                array[j] = array[j + 1];
                array[j + 1] = t;
            }
        }
    }
    return array;
}

// set array length to 50 with random elements
const arrayLength = 50;
const array = [];
for (let i = 0; i < arrayLength; i++) {
    array.push(Math.floor(Math.random() * 10000) + 1)
}

bubbleSort(array);
console.time(array);
console.timeEnd(array);
