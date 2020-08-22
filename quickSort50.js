// quickSort50.js
// Quick sort algorithm written in JavaScript with Temporal Analysis for 50 random array elements
// NCU.edu
// School of Business & Technology Managment
// TIM-6110
// Author: Ravi Jethva
// Date: August 23, 2020

// set array length to 50, random elements inserted to array
const arrayLength = 50;
const array = [];
for (let i = 0; i < arrayLength; i++) {
    array.push(Math.floor(Math.random() * 10000) + 1)
}

// display quick sorted array with temporal analysis
console.time(array.sort());
console.timeEnd(array.sort());
