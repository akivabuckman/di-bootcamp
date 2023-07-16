const form = document.querySelector("form");
const [username, password] = ["username", "password"].map(id => document.getElementById(id));
const messageBox = document.getElementById("message")
form?.addEventListener("submit", handleSubmit);

const url = "http://localhost:3000/login";

function handleSubmit(e) {
    e.preventDefault();
    if (username.value === "" || password.value === "") return;
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            password: password.value, 
            username: username.value})
    }
    fetch(url, options)
        .then(res=>res.json())
        .then(res=> messageBox.textContent=res.message)
        .catch(console.error)
}