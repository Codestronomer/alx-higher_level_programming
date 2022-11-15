#!/usr/bin/node
const request = require('request');
// get starwars title from episode passed in argument
request(process.argv[2],
  (err, response, body) => {
    if (err == null) {
      const res = JSON.parse(response.body);
      // console.log(res.results);
      let movieCount = 0;
      res.results.forEach(movie => {
        movie.characters.forEach(actor => {
          if (actor.includes('18')) {
            movieCount++;
          }
        });
      });
      console.log(movieCount);
    }
  });
