#!/usr/bin/node

const x = parseInt(process.argv[2], 10);

if (isNaN(x)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + x);
}
