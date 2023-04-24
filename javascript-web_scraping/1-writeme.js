#!/usr/bin/node
//writes a string to a file.
const path = process.argv[2];
const text = process.argv[3];
const fs = require('fs');
fs.writeFile(path, text, 'utf-8', (err, data)=>{
    if(err){
        throw err;
    }
    console.log(data);
})
