#!/usr/bin/node
const fs = require('fs');
const process = require('process');

// opens file passed as argument
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});
