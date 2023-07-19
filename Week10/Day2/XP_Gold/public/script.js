document.querySelector("form").addEventListener("submit", handleSubmit);

async function handleSubmit(e) {
    e.preventDefault()
    const form = document.querySelector("form");
    const formData = new FormData(form);
    const formEntries = Array.from(formData.entries());
    const formDataObject = Object.fromEntries(formEntries);
    const jsonData = JSON.stringify(formDataObject);
    try {
        const res = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: jsonData
        });
        const data = await res.json();
        console.log("data", data);
        const newh3 = document.createElement("h3");
        newh3.textContent = JSON.stringify(data);
        document.body.appendChild(newh3);
    } catch (err) {
        console.error(err)
    }
}