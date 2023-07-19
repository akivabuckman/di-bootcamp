async function getItems() {
    try {
        const response = await fetch("/getItems");
        console.log(response)
        let data = await response.json();
        console.log(data);
        const ol = document.querySelector("#itemList");
        const itemList = data;
        let cont = "";
        for (let i of itemList) {
            for (let k in i) {
                cont += `<li>${k}: $${i[k]}</li>`
            }
        };
        ol.innerHTML = cont;
    } catch(err) {
        console.error(err)
    }
};

getItems();

document.querySelector("form").addEventListener("submit", handleSubmit);
async function handleSubmit(e) {
    // e.preventDefault()
    const form = document.querySelector("form");
    const formData = new FormData(form);
    const formEntries = Array.from(formData.entries());
    const formDataObject = Object.fromEntries(formEntries);
    const jsonData = JSON.stringify(formDataObject);
    try {
        const res = await fetch("/items", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: jsonData
        });
        const data = await res.json();
        console.log("data", data);


    } catch (err) {
        console.error(err)
    }
};