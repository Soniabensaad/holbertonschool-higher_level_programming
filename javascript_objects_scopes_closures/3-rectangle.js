#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w <= 0 || !Number.isInteger(w) || h <= 0 || !Number.isInteger(h)) {
        return this;
      }
      this.width = w;
      this.height = h;
    }
    print() {
        for (let i = 0; i < this.height ; i++){
            let row ="";
            for (let j = 0; i< this.width; j++){
                 row += "X";

            }
            console.log (row);
        }
    }
  }
  
  module.exports = Rectangle;
  