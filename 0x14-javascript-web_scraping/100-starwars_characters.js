#!/usr/bin/node
const request = require('request');
// get starwars title from episode passed in argument
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err == null) {
      const res = JSON.parse(response.body);
      res.characters.forEach(url => {
        request(url, (err, response, body) => {
          if (err == null) {
            const res = JSON.parse(response.body);
            console.log(res.name);
          }
        });
      });
    }
  });