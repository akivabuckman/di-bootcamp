const express = require('express');
const app = express();
const cors = require("cors");
app.use(cors())
app.use(express.json())

app.get('/api/hello', (req, res) => res.json({msg:"hi there fro express"}))

app.post("/api/world", (req, res) => {
    console.log(req.body);
    res.send({message: `I got your post. this is it: ${req.body.userInput}`})
})




app.listen(3000, () => {
    console.log('server is listening in port 3000')
});