#!/usr/bin/node
const request = require('request');
const process = require('process');

// opens gets response statusCode from url passed as argument
request(process.argv[2], (err, response, body) => {
  if (err) { console.log(err); }
  console.log('code: ', response && response.statusCode);
});
