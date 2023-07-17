const express = require('express');
const knex = require('knex');
const bcrypt = require('bcrypt');

const app = express();
const db = knex({
  client: 'pg',
  connection: {
    host: 'localhost',
    user: 'akiva',
    password: '1234',
    database: 'w10d4xp',
  },
});

app.use(express.urlencoded({ extended: false }));

// Register route
app.post('/register', (req, res) => {
  const { firstName, lastName, email, username, password } = req.body;

  // Check if email already exists
  db.select('*')
    .from('register')
    .where('email', '=', email)
    .then(rows => {
      if (rows.length > 0) {
        res.send('Email already exists');
      } else {
        // Encrypt the password
        const hashedPassword = bcrypt.hashSync(password, 10);

        // Insert the user into the register table
        db('register')
          .insert({
            first_name: firstName,
            last_name: lastName,
            email,
            username,
            password: hashedPassword,
            created_date: new Date(),
            last_login_date: null,
          })
          .then(() => {
            res.send('Registration successful');
          })
          .catch(error => {
            res.send('Registration failed');
          });
      }
    })
    .catch(error => {
      res.send('An error occurred');
    });
});

// Login route
app.post('/login', (req, res) => {
  const { loginUsername, loginPassword } = req.body;

  // Retrieve the user from the register table
  db.select('*')
    .from('register')
    .where('username', '=', loginUsername)
    .then(rows => {
      if (rows.length > 0) {
        // Compare the passwords
        const isValidPassword = bcrypt.compareSync(loginPassword, rows[0].password);
        if (isValidPassword) {
          // Update the last login date in the register table
          db('register')
            .where('username', '=', loginUsername)
            .update('last_login_date', new Date())
            .then(() => {
              res.send('Login successful');
            })
            .catch(error => {
              res.send('Login failed');
            });
        } else {
          res.send('Invalid password');
        }
      } else {
        res.send('User does not exist');
      }
    })
    .catch(error => {
      res.send('An error occurred');
    });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
