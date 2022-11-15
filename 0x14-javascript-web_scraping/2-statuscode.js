#!/usr/bin/node
const request = require('request');
// opens gets response statusCode from url passed as argument
request(process.argv[2], (err, response, body) => {
  if (err == null) {
    console.log('code: ' + response.statusCode);
  }
});
