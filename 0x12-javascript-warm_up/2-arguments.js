#!/usr/bin/node
const argumentsNum = process.argv.length;
if (argumentsNum <= 2) {
	console.log('No argument');
} else if (argumentsNum === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
