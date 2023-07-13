// XP3
const express = require("express");
const app = express();

app.listen(3000, () => {
    console.log("on 3000");
});

app.get('', (req, res) => {
    res.write("<h1>hi</h1>")
})