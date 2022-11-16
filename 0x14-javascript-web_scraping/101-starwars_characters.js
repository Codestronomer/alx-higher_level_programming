#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err == null) {
      const res = JSON.parse(body).characters;
      const i = 0;
      printActor(res, i);
    }
  });

function printActor (characters, i) {
  const actor = characters[i];
  if (actor) {
    request(actor, (err, response, body) => {
      if (err == null) {
        const res = JSON.parse(body);
        console.log(res.name);
        i = i + 1;
        printActor(characters, i);
      }
    });
  }
}
