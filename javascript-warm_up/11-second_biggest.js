#!/usr/bin/node
//searches the second biggest integer in the list of argument
if(process.argv.length<= 3){
    console.log(0);
}
else{
    const rst = (process.argv.sort());
    console.log(rst.reverse()[1]);
}
