#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, function (error, response) {
  if (error == null) {
    
    console.log(`code: ${response.statusCode}`);
  }
});
