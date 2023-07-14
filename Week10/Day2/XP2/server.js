const express = require("express");
const app = express();
const user = {firstname: 'John',lastname: 'Doe'}

app.listen(3000, ()=>{console.log("on 3000")});


app.get("/users", (req, res) => {
    console.log(JSON.stringify(user))
    res.sendFile(__dirname + '/public/index.html');
});

// Create a route /, and use a GET request method.
// The path of the route should contain the route parameter id.
// The handler function of the route should respond with the value of the route parameter. Check out req.params.

// app.get("/:id", (req, res) => {
//     console.log(req.params);
//     res.json(req.params);
// });

app.get("/", (req, res) => {
    res.sendFile(__dirname + '/public/xp3.html');
});

