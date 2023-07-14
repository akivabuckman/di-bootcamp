// XP1
fetch("/users")
.then(res => res.json())
.then(data => {
    console.log(data);
    console.log(1)
    document.querySelector("#result").innerHTML= `<p>${JSON.stringify(data)}</p>`;
})
.catch((e) => {
    console.log(e)
});