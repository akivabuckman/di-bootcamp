const express = require("express");
const app = express();
app.listen(3000, ()=> {console.log("server.js on 3000")});
app.use(express.urlencoded({ extended: true}));
app.use(express.json());

app.use("/", express.static(__dirname + "/public"));

const itemList = [{"apples": 3}, {"fufu": 43}];

app.get('/items', (req, res) => {
    res.sendFile(__dirname + "/public/index.html")
});

app.get("/getItems", (req, res) => {
    res.send(JSON.stringify(itemList))
});


app.get("/items/:id", (req, res) => {
    const id = req.params.id;
    const key = Object.keys(itemList[id])[0];
    res.send(`<h1>${key}: $${itemList[id][key]}</h1>`)
});

app.post("/items", (req, res) => {
    const str = `{"${req.body.food}": "${req.body.price}"}`;
    const obj = JSON.parse(str)
    console.log(obj)
    itemList.push(obj);
    res.json({response: itemList})  
})