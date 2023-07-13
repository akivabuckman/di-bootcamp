// XP1
// In this file, use http to create a server. You should return at least three different lines of HTML to the browser. (Use only HTML tags, no HTML files)
// Your server should run on http://localhost:3000/

const { log } = require("console");
const http = require("http");

const server = http.createServer((req, res) => {
  res.write('<h1>Node.js is crazy</h1>');
  res.write('<p>Not banging my head against a wall at all</p>');
  res.write('<a href="https://www.google.com">Click here</a> to visit google.com');

  // End the response
  res.end();
});

server.listen(3000, () => {
});

