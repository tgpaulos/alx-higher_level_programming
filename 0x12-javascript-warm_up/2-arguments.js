#!/usr/bin/node

// Get the number of arguments passed
const numArgs = process.argv.length - 2;

// Print the message based on the number of arguments
if (numArgs === 0) {
    console.log("No argument");
} else if (numArgs === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
