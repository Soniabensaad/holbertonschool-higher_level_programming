#!/usr/bin/node

const Rectangle = require('./5-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
  charPrint() {
    
        for (let i = 0; i < this.height; i++) {
          let row = '';
          for (let j = 0; j < this.width; j++) {
            let C;
            if (C === undefined){
                row += 'X';
            }
            else{

                row += 'C';
            }
          console.log(row);
        
  }
}
}
}

module.exports = Square;
