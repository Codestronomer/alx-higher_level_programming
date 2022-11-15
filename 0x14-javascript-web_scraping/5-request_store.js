#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err == null) {
    fs.writeFilesync(process.argv[3], body);
  }
});
