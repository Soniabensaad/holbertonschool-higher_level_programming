#!/usr/bin/node
//number of movies where the character “Wedge Antilles” is present
const request = require('request');
const id = 18;
const url = `https://swapi-api.hbtn.io/api/people/${id}/`;

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    const filmsUrl = JSON.parse(body).films;
    const filmsCount = filmsUrl.length;
    console.log(filmsCount);
});
