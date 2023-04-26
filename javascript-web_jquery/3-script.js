#!/usr/bin/node
// adds the class red to the <header> element when the user
// clicks on the tag DIV#red_header
const $head = $('header');
const $div = $('DIV#red_header');
$("div").click(function(){
    $("head").addClass("red");
});
