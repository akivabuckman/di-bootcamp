const express = require("express");
const app = express();
const port = 3000;
app.use(express.json());
app.listen(port, ()=> console.log("listening on port 3000"));
app.use('/', express.static(__dirname + '/public'));

app.post("/register", registerFunc);
app.post("/login", loginFunc);

const db = require("knex") ({
    client: 'pg',
    connection: {
      host: 'localhost',
      user: 'postgres',
      password: '1234',
      database: 'w10d4xp',
    },
  });

app.set("db", db);
// app.get('/db', (req, res) => {
//     db
//     .select().from("login")
//     .then(whatever=> res.send(whatever))
// })


async function registerFunc(req, res) {
    if (!isRequestValid(req.body)) return res.status(400).send({ message: "mistake in given params" });
  
    try {
      const rows = await db.select("username").from("register");
      const usernames = rows.map(row => row.username);
      if (usernames.includes(req.body.username)) {
        return res.status(400).send({ message: "Username already exists" });
        } else {
        await db("register").insert({
          first_name: req.body.firstname,
          last_name: req.body.lastname,
          email: req.body.email,
          username: req.body.username,
          password: req.body.password
        });
        return res.send({ message: `Hi ${req.body.firstname}, your username is ${req.body.username}` });
        }
    } catch (error) {
      if (error.message === "Username already exists") {
        return res.status(400).send({ message: "Username already exists" });
        } else {
        console.error('An error occurred:', error);
        return res.status(500).json({ success: false, message: "Registration failed" });
        }
    }
};


function isRequestValid(body) {
    const {firstname, lastname, email, username, password} = body;
    if (isAnyFieldEmpty([firstname, lastname, email, username, password])) return false;
    return true;
};

function isAnyFieldEmpty(inputs) {
    return inputs.some(input => input === "" || input == null)
};

async function loginFunc(req, res) {
    try {
        // given data
        const usernameGuess = req.body.username;
        const passwordGuess = req.body.password;
        if (usernameGuess == null || usernameGuess.length === 0) {
            return res.status(400).send({message: "username cant be blank"})
        };
        if (passwordGuess == null || passwordGuess.length === 0) {
            return res.status(400).send({message: "password cant be blank"})
        };
        // db data
        const rows = await db.select("username", "password").from("register");
        // const usernames = rows.map(row => row.username);
        const usernames = rows.map(obj => obj.username);
        if (!usernames.includes(req.body.username)) {
            return res.status(400).send({message: "That username doesn't exist"})
        };
        const correctPassword = await db.select("password").from("register").where({username: req.body.username});
        if (req.body.password != correctPassword) {
            return res.status(400).send({message: "incorrect password"})
        };

        // if success
        if (req.body.password === correctPassword) {
            await db("login").insert({
                username: req.body.username,
                password: req.body.password
            })
        }

    } catch (error) {
            if (error.message === "Username already exists") {
            return res.status(400).send({ message: "Username already exists" });
            } else {
            console.error('An error occurred:', error);
            return res.status(500).json({ success: false, message: "Registration failed" });
            }
    }
};