// Part 1
const {largeNumber, getCurrentDate} = require('./main.js');

const b = 5;

console.log(largeNumber + b);

// Part 2
let http = require("http");
const server = http.createServer(responseHandler);
const port = 3000;
const host = "localhost";
function func() {
    console.log("I'm listening")
};
server.listen(port, host, func);

function responseHandler(req, res) {
    console.log('request: ', req);
    console.log('response: ', res);
    res.setHeader('Content-Type', 'text/html');
    res.end(`
        <h1>Response from server</h1>
        <p> The large number is ${largeNumber})</p>`);
    res.writeHead(201);
};

// Part 3
function part3Response(req, res) {
    console.log('request: ', req);
    console.log('response: ', res);
    res.setHeader("Content-Type", "text/html");
    res.writeHead(200);
    res.end(`
        <p>The date and time are currently: ${getCurrentDate()}</p>
        `);
};

const newServer = http.createServer(part3Response);
const newPort = 8080;
newServer.listen(newPort, host, func);
