const searchForm = document.getElementById('titleForm');

searchForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const ol = document.querySelector("#results");
    ol.innerHTML = ''
    const searchInput = searchForm.titleSearch.value.trim();
    const data = await fetchTitle(searchInput); // array of objects
    if (data.length === 0) {
        const messageBox = document.querySelector("#message");
        messageBox.textContent = `No results for "${searchInput}"`
    }  else {
        for (let i of data) {
        let newLi = document.createElement("li");
        let newA = document.createElement("a");
        newA.textContent = i.title;
        newA.setAttribute("style", "color:turquoise; font-size: 24px; text-decoration: none;");
        newA.setAttribute("href", i.link)
        let infoP = document.createElement("p");
        let previewP = document.createElement("p");
        previewP.textContent = i.contentSnippet;
        let infoSpan = document.createElement("span");
        infoSpan.textContent = `${i.pubDate} | ${i.creator} | Categories: `;
        let categorySpan = document.createElement("span");
        categorySpan.textContent = i.categories.join(', ')
        categorySpan.setAttribute("style", "font-weight: bolder")
        infoP.appendChild(infoSpan);
        infoP.appendChild(categorySpan);
        newLi.appendChild(newA);
        newLi.appendChild(infoP);
        newLi.appendChild(previewP)
        ol.appendChild(newLi);
        }
    }
    
});

async function fetchTitle(searchInput) {
    try {
        const response = await fetch("/search/title", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({searchInput: searchInput})
        });
        const data = await response.json()
        return data
    } catch(err) {
        console.error(err)
    }
};


// CATEGORY SEARCH
const categoryForm = document.getElementById('categoryForm');
categoryForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const ol = document.querySelector("#results");
    ol.innerHTML = ''
    const categoryInput = categoryForm.categorySearch.value.trim();
    const data = await fetchCategory(categoryInput); // array of objects
    if (data.length === 0) {
        const messageBox = document.querySelector("#message");
        messageBox.textContent = `No results for "${categoryInput}"`
    } else {
        for (let i of data) {
        let newLi = document.createElement("li");
        let newA = document.createElement("a");
        newA.textContent = i.title;
        newA.setAttribute("style", "color:turquoise; font-size: 24px; text-decoration: none;");
        newA.setAttribute("href", i.link)
        let infoP = document.createElement("p");
        let previewP = document.createElement("p");
        previewP.textContent = i.contentSnippet;
        let infoSpan = document.createElement("span");
        infoSpan.textContent = `${i.pubDate} | ${i.creator} | Categories: `;
        let categorySpan = document.createElement("span");
        categorySpan.textContent = i.categories.join(', ')
        categorySpan.setAttribute("style", "font-weight: bolder")
        infoP.appendChild(infoSpan);
        infoP.appendChild(categorySpan);
        newLi.appendChild(newA);
        newLi.appendChild(infoP);
        newLi.appendChild(previewP)
        ol.appendChild(newLi);
    }
    }
    
});

async function fetchCategory(searchInput) {
    try {
        const response = await fetch("/search/category", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({searchInput: searchInput})
        });
        const data = await response.json()
        return data
    } catch(err) {
        console.error(err)
    }
}