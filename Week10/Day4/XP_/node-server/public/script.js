// register
const registerIds = ["firstName", "lastName", "email", "username", "password"];
const registerInputTags = registerIds.map(id=> document.getElementById(id));
const registerButton = document.getElementById("registerBtn");
const registerForm = document.querySelector("#registerForm");
registerForm.addEventListener("submit", handleRegistration);
const url = "http://localhost:3000"
const messageBox = document.querySelector("#messageBox")
function handleChange(tags, button) {
    if (tags.some(input => input.value === "")) {
        button.disabled = true;
    } else {
        button.disabled = false
    }
};

registerInputTags.forEach(input => input?.addEventListener("input", ()=> handleChange(registerInputTags, registerButton)));

function handleRegistration(e) {
    const [firstName, lastName, email, username, password] = registerInputTags;
    e.preventDefault();
    const body = {
        firstname: firstName.value,
        lastname: lastName.value,
        email: email.value,
        username: username.value,
        password: password.value,
    };
    const options = {
        headers: {
            "Content-Type": "application/json"
        },
        method: "POST",
        body: JSON.stringify(body)
    };
    fetch(`${url}/register`, options)
        .then(res => res.json())
        .then(res=> messageBox.textContent=res.message)
        .catch(error => {
            messageBox.textContent=res.message
        })
};



// login
const loginIds = ["loginUsername", "loginPassword"];
const loginInputTags = loginIds.map(id=> document.getElementById(id));
const loginButton = document.getElementById("loginBtn");
const loginForm = document.querySelector("#loginForm");
loginForm.addEventListener("submit", handleLogin);
function handleChange(tags, button) {
    if (tags.some(input => input.value === "")) {
        button.disabled = true;
    } else {
        button.disabled = false
    }
};

loginInputTags.forEach(input => input?.addEventListener("input", ()=> handleChange(loginInputTags, loginButton)));

function handleLogin(e) {
    const [username, password] = loginInputTags;
    e.preventDefault();
    const body = {
        username: username.value,
        password: password.value,
    };
    const options = {
        headers: {
            "Content-Type": "application/json"
        },
        method: "POST",
        body: JSON.stringify(body)
    };
    fetch(`${url}/login`, options)
        .then(res => res.json())
        .catch(error => {
            messageBox.textContent=res.message
        })
    }
