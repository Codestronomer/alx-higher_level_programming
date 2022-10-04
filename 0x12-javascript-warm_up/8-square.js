#!/usr/bin/node

const argv = process.argv[2];

if (parseInt(argv)) {
  for (let i = 0; i < parseInt(argv); i++) {
    for (let j = 0; j < parseInt(argv); j++) {
      process.stdout.write('x');
    }
    console.log('');
  }
} else {
  console.log('Missing size');
}
