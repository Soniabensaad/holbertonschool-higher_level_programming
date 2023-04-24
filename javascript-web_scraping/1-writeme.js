#!/usr/bin/node
//writes a string to a file.
const fs = require('fs');

const filePath = process.argv[2];
const textToWrite = process.argv[3];

fs.writeFile(filePath, textToWrite, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
})
