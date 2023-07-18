document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;

    fetch("/formData", {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({ email: email, message: message })
    })
    .then(response => response.text())
    .then(data => {
    console.log(data);
    document.getElementById("contactForm").reset();
    alert(data);
    })
    .catch(error => {
    console.error(error);
    alert("An error occurred. Please try again.");
    });
});
