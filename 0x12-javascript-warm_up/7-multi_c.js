#!/usr/bin/node

const argv = process.argv;

if (parseInt(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
}
