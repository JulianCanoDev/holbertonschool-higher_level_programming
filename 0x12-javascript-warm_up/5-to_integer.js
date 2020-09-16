#!/usr/bin/node
// Number
const NUM = parseInt(process.arg[2]);
if (Number.isInteger(NUM)) {
    console.log('My number: ' + NUM);
} else {
    console.log('Not a number');
}
