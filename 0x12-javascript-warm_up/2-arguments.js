#!/usr/bin/node
const args = process.argv;
const l = args.length;
if (l === 2) {
  console.log('No argument');
} else if (l === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
