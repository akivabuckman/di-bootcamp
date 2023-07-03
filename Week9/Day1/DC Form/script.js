document.querySelector("form").addEventListener('submit', submitFunc);

function submitFunc(e) {
    e.preventDefault();
    const data = new FormData(document.querySelector("form"));
    const entries = data.entries();
    const dataObject = Object.fromEntries(entries);
    dataString = JSON.stringify(dataObject);
    const newP = document.createElement('p');
    newP.textContent = dataString;
    document.body.appendChild(newP);
}