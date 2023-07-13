const express = require("express");
const app = express();
const user = {firstname: 'John',lastname: 'Doe'}

app.listen(3000, ()=>{console.log("on 3000")});

app.get("/users", (req, res) => {
    res.json(user);
});

app.use('/', express.static(__dirname + '/public'));