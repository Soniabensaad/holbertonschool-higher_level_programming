#!/usr/bin/node
exports.esrever = function (list) {
  const c = [];
  for (let i = list.length - 1; i >= 0; i--) {
    c.push(list[i]);
  }
  return (c);
};
