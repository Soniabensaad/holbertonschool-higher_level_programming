#!/usr/bin/node
//script that computes and prints a factorial
function factorial(n){
    if(isNaN(parseInt(n))){
        return ('argument can be cast as integer');
    }
    if(n==0 || n==1){
        return 1;
    }
    else{
        return n*factorial(n-1);
    }
    
}
function print(start, end){
    if (start>end){
        return ;
    }
    else{
        console.log(factorial(start));
        print(start + 1, end);
    }
}
