// XP2
const user = {
    firstname: 'John',
    lastname: 'Doe'
};

const {log} = require("console");

const http = require("http");

const server = http.createServer((req, res) => {
    res.end(JSON.stringify(user));
});

server.listen(8080, () =>{});