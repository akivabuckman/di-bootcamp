const express = require("express");
const app = express();
app.listen(3000, ()=> {console.log("server.js on 3000")});
app.use(express.urlencoded({ extended: true}));
app.use(express.json());

app.use("/", express.static(__dirname + "/public"));

app.post("/", (req, res) => {
    console.log(req.body);
    res.json({response: req.body})
})