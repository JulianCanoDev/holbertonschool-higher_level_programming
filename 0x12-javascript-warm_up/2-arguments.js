#!/usr/bin/node
// Count arguments
const myArgs = process.argv.lengh;
if (myArgs === 2) {
  console.log('No argument');
} else if (myArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
