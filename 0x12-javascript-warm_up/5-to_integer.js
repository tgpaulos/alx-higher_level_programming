#!/usr/bin/node

// Assuming the first argument is passed as a command line argument
const arg1 = process.argv[2];

// Convert the argument to an integer
const num = parseInt(arg1);

// Check if the conversion was successful
if (!Number.isNaN(num)) {
    // Print the formatted output
    console.log('My number: ' + num);
} else {
    // Print "Not a number"
    console.log("Not a number");
}
