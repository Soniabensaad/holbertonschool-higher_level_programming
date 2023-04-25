#!/usr/bin/node
//pdates the text color of the <header> 
//element to red (#FF0000) when the user 
//clicks on the tag DIV#red_header

    
    $("DIV#red_header").on("click", function() {
    
      $("header").css("color", "#FF0000");
    });
 
