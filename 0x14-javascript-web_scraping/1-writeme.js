#!/usr/bin/node
const fs = require('fs');
const process = require('process');

// opens file passed as argument
fs.writeFile(process.argv[2], process.argv[3], err => {
  if (err) {
    console.log(err);
  }
});
