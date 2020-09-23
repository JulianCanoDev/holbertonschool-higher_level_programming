#!/usr/bin/node
// Read files
var fs = require('fs');

try {
  const data = fs.readFileSync(process.argv[2], 'utf8');
  console.log(data.toString());
} catch (e) {
  console.log('Error:', e.stack);
}
