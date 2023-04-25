#!/usr/bin/node
// number of movies where the character “Wedge Antilles” is present
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const numFilmsWithWedgeAntilles = films.filter(film => {
      return film.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`);
    }).length;
    console.log(numFilmsWithWedgeAntilles);
  }
});
