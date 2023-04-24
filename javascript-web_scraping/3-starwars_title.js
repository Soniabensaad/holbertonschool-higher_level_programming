#!/usr/bin/node
// prints the title of a Star Wars movie where
// the episode number matches a given integer.
const request = require('request');
const episode = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${episode}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const titleMovie = JSON.parse(body);
    console.log(titleMovie.title);
  }
});
