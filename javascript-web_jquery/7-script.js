#!/usr/bin/node
//fetches the character name from this
// URL: https://swapi-api.hbtn.io/api/people/5/?format=json
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
          $('#character').text(data.name);
});
