#!/usr/bin/node
//toggles the class of the <header> element when the user
// clicks on the tag DIV#toggle_header
const $headi = $('header');
const $div = $('DIV#toggle_header');
$("div").click(function(){
    if($headi.hasClass("red")){
        $headi.removeClass("red").addClass("green");
    } else {
        $headi.removeClass("green").addClass("red");
    }
    
});
