#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err == null) {
    if (response && response.statusCode === 200) {
      fs.writeFile(process.argv[3], body, (err) => {
        if (err) { console.log(err); }
      });
    }
  }
});
