#!/usr/bin/node
//computes the number of tasks completed by user id.
const request = require('request');

const url = "https://jsonplaceholder.typicode.com/todos";
request(url, (error, response, body)=>{
    if(error){
        console.log(error);
    }
    else {
        const todos = JSON.parse(body);
        const completed = {};
        todos.forEach(todo => {
            if(todo.completed){
                const userId = todo.userId;
                completed[userId] = (completed[userId] ||0)+1;
            }
        });
        for (const [userId, count] of Object.entries(completed)) {
            console.log(`${userId}: ${count}`);
        }
    }
});
