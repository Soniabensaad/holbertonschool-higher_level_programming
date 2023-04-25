#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf8' }, function (err) {
      if (err) {
        console.error(err);
      }
    });
  }
});
