const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');

const app = express();

app.listen(3000, () => {
    console.log('server is listening in port 3000')
});

app.use('/', express.static(__dirname + '/public'));

app.get('/projects', (req, res) =>{
    res.sendFile(__dirname + '/public/projects.html')
})


// Parse incoming request bodies in a middleware
app.use(bodyParser.urlencoded({ extended: true }));

// Serve your static files (HTML, CSS, JS)
app.use(express.static('public')); // Change 'public' to your static files directory

// Set up your email transporter
const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'akivabuckman@gmail.com',
    pass: env.emailpassword
  }
});

// Handle form submissions
app.post('/submit-form', (req, res) => {
  const name = req.body.name;
  const email = req.body.email;
  const message = req.body.message;

  const mailOptions = {
    from: email,
    to: 'your-email@example.com', // Your email address
    subject: 'New Contact Form Submission',
    text: `Name: ${name}\nEmail: ${email}\nMessage: ${message}`
  };

  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.error(error);
      res.status(500).send('Error sending email');
    } else {
      console.log('Email sent: ' + info.response);
      res.status(200).send('Email sent successfully');
    }
  });
});

