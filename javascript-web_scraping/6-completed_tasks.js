#!/usr/bin/node
//computes the number of tasks completed by user id.

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const completedByUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedByUser[todo.userId]) {
        completedByUser[todo.userId] += 1;
      } else {
        completedByUser[todo.userId] = 1;
      }
    }
  });

  console.log(completedByUser);
});
