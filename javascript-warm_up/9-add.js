#!/usr/bin/node
//prints the addition of 2 integers
const add = (a, b) => {
    if (!isNaN(a) && !isNaN(b)) {
      console.log(a + b);
    } else {
      console.log("NaN");
    }
  }
  
  const a = parseInt(process.argv[2]);
  const b = parseInt(process.argv[3]);
  
  add(a, b);
  
