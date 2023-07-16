const ids = ["firstname", "lastname", "email", "username", "password"];

const divs = ids.map(id=> document.getElementById(id));
const submitButton = document.getElementById("submit");
const [firstname, lastname, email, username, password] = divs;
const form = document.querySelector("form");
const url = "http://localhost:3000/register";
const messageBox = document.querySelector("#message");
divs.forEach(div => div?.addEventListener("input", handleChange));
form?.addEventListener("submit", handleSubmit)

function handleChange(e) {
    if (divs.some(div => div.value === "")) {
        submitButton.disabled = true;
    } else {
        submitButton.disabled = false
    }
};

function handleSubmit(e) {
    const [firstname, lastname, email, username, password] = divs;

    e.preventDefault();
    const body = {
        firstname: firstname.value,
        lastname: lastname.value,
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
    fetch(url, options)
        .then(res => res.json())
        .then(res => messageBox.innerText = res.msg)
        .catch(console.error)
    }