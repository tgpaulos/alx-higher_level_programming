#!/usr/bin/node

// Get the first argument passed to the script
const firstArg = process.argv[2];

// Print the appropriate message if  an argument is provided
if (firstArg) {
    console.log(firstArg);
} else {
    console.log("No argument");
}
