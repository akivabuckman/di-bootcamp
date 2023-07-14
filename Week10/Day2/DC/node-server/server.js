const express = require("express");
const app = express();
const bodyParser = require("body-parser")
app.use(bodyParser.urlencoded({ extended: true }));

app.listen(3000, () => {console.log('server.js listening on 3000')});

// The route /aboutMe/:hobby sends the name of one hobby (ie. the value of the route parameter). If the parameter is not a string (ie. numbers or else), set the status to 404.
app.get('/aboutMe/:hobby', (req, res) => {
    const hobby = req.params.hobby;
    if (isNaN(hobby)) {res.send(req.params)} else {res.sendStatus(404)};
});

// The route /pic : displays an HTML file with a picture of your choice.
app.get("/pic", (req, res) => {
    res.sendFile(__dirname + '/public/pic.html')
});


// The route /form: displays an HTML file.
// Requirements:
// The HTML file must be in the public folder.
// The HTML file must contain a form to contact you.
// The form must contain the inputs email and message. (add some HTML form validations)
// Output:
// You should get the data and display it on the browser at the route /formData.
// For example, “john@gmail.com sent you a message “Love your new website”
app.get("/form", (req, res) => {
    res.sendFile(__dirname + '/public/form.html')
});

app.post("/formData", (req, res) => {
    const email = req.body.email;
    const message = req.body.message;
    res.send(`${email} sent you a message: "${message}"`);
});