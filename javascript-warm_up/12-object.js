#!/usr/bin/node
// replace the value 12 with 89
const myObject = {
    type: 'object',
    value: 12
  };
  
  console.log(myObject);
  
  const newObj = {
    ...myObject, 
    value: 89 
  };
  
  console.log(newObj);
