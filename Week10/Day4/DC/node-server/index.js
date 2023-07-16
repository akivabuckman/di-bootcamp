const express = require("express");
const cors = require("cors");
const app = express();
const port = 3000;
const users = [];
app.use(express.json());
app.use(cors())
app.post("/register", createUser)
app.post("/login", login)
app.listen(port, ()=> console.log(`listening on ${port}`));

function createUser(req, res) {

    if (!isRequestValid(req.body)) return res.status(400).send({message: "mistake in given params"});
    if (users.some(user => user.username === req.body.username)) {
        return res.status(400).send("user already exists")
    };
    const newUser = {
        username: req.body.username,
        password: req.body.password
    };
    users.push(newUser);
    res.send({msg: "your account is now created"})

};

function isRequestValid(body) {
    const {firstname, lastname, email, username, password} = body;
    if (isAnyFieldEmpty([firstname, lastname, email, username, password])) return false;
    return true;
};

function isAnyFieldEmpty(inputs) {
    return inputs.some(input => input === "" || input == null)
};

function login(req, res) {
    const username = req.body.username;
    const password = req.body.password;
    if (username == null || username.length === 0) {
        return res.status(400).send({message: "username cant be blank"})
    };
    if (password == null || password.length === 0) {
        return res.status(400).send({message: "password cant be blank"})
    };
    const user = getUserfromArray(username);
    if (user == null) {
        return res.status(400).send({message: "user not found"})
    };
    if (user.password != password) {
        return res.status(400).send({message: "wrong password"})
    };
    res.send({"msg": `Hi ${username} welcome back`})

};
function getUserfromArray(username) {
    return users.find(user => user.username === username);
};
