#!/usr/bin/node
// fetches from https://stefanbohacek.com/hellosalut/?lang=fr
// and displays the value of hello from that
 //fetch in the HTML tag DIV#hello.
 $.get("https://stefanbohacek.com/hellosalut/?lang=fr", function(data) {
    var hello = $(data).find("div#hello").text();
    $("div#hello").text(hello);
  });
