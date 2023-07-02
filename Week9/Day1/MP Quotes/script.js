let quotes = [];
let quoteInputs = ["i like cake", "i love pasta", "i hate onions"];
let authors = ["akiva buckman", "akiva gladwell", "jk akiva"];

for (let i = 0; i < 3; i++) {
    quotes.push(
        {
            "id": i,
            "author": authors[i],
            "quote": quoteInputs[i],
            "likes": 0
        }
    );
}

// assign function to the quote button
document.getElementById('quoteButton').addEventListener("click", generateQuote);



function generateQuote() {
    let randomIndex;
    if (typeof previous == 'undefined') {
        randomIndex = Math.floor(Math.random() * quotes.length);
        let previous;
    } else {
        do {
            randomIndex = Math.floor(Math.random() * quotes.length);
        } while (randomIndex === previous);
    }
    previous = randomIndex;
    const parent = document.getElementById("quoteBox");

    // remove pre-existing quote elements
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    };
    let newP = document.createElement('p');
    let authP = document.createElement('p');
    newP.setAttribute('id', 'quote');
    authP.setAttribute('id', 'author');
    newP.textContent = quotes[randomIndex]['quote'];
    authP.textContent = quotes[randomIndex]['author'];
    parent.appendChild(newP);
    parent.appendChild(authP);
};

document.getElementById('addButton').addEventListener("click", addQuote);

function addQuote() {
    const newQuote = document.forms.newQuote.quote.value;
    const newAuth = document.forms.newQuote.author.value;
    const idList = quotes.map((value, index, array) => {
        return value.id
    });
    const maxId = Math.max(...idList);
    quotes.push({
        "id": maxId + 1,
        "quote": newQuote,
        "author": newAuth,
        "likes": 0
    });
}


document.getElementById('charButton').addEventListener("click", displayChars);

function displayChars() {
    const parent = document.getElementById('quoteParams');
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    };
    let newP = document.createElement('p');
    newP.setAttribute('id', 'paramData');
    const quote = document.getElementById('quote').textContent;
    newP.textContent = `Total characters: ${quote.length}`;
    parent.appendChild(newP);
};

document.getElementById('NoSpaceButton').addEventListener("click", displayNoBlank);

function displayNoBlank() {
    const parent = document.getElementById('quoteParams');
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    };
    let newP = document.createElement('p');
    newP.setAttribute('id', 'paramData');
    const quote = document.getElementById('quote').textContent;
    newP.textContent = `Non-space characters: ${quote.replace(/ /g, '').length}`;
    parent.appendChild(newP);
};

document.getElementById('wordButton').addEventListener("click", displayWords);

function displayWords() {
    const parent = document.getElementById('quoteParams');
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    };
    let newP = document.createElement('p');
    newP.setAttribute('id', 'paramData');
    const quote = document.getElementById('quote').textContent;
    newP.textContent = `Words: ${quote.split(' ').length}`;
    parent.appendChild(newP);
};

document.getElementById('likeButton').addEventListener("click", like);

function like() {
    const quoteText = document.getElementById('quote').textContent;
    for (let i of quotes) {
        if (i.quote == quoteText) {
            i.likes += 1;
        };
    }
}

document.getElementById('searchButton').addEventListener("click", searchAuthors);

function searchAuthors() {
    let entry = document.getElementById('authorSearch').authorEntry.value.toLowerCase();
    if (entry != '') {
        let newQuotes = quotes.filter(i => i.author.toLowerCase().includes(entry));
        const parent = document.getElementById('searchResults');
        while (parent.firstChild) {
            parent.removeChild(parent.firstChild);
        };
        let newP = document.createElement('p');
        newP.setAttribute('id', 'searchResult');
        newP.textContent = newQuotes[0]['quote'];
        parent.appendChild(newP);

        let authorP = document.createElement('p');
        authorP.setAttribute('id', 'authorResult');
        authorP.textContent = newQuotes[0]['author'];
        parent.appendChild(authorP);

        if (newQuotes.length > 1) {
            let PreviousButton = document.createElement('input');
            PreviousButton.setAttribute('type', 'button');
            PreviousButton.setAttribute('value', 'Previous');
            PreviousButton.addEventListener('click', PreviousQuote);
            parent.appendChild(PreviousButton);
            
            let nextButton = document.createElement('input');
            nextButton.setAttribute('type', 'button');
            nextButton.setAttribute('value', 'Next');
            nextButton.addEventListener('click', nextQuote);
            parent.appendChild(nextButton);
        };
    };
}

function nextQuote() {
    let currentQuote = document.getElementById('searchResult');
    let currentAuth = document.getElementById('authorResult');
    let entry = document.getElementById('authorSearch').authorEntry.value.toLowerCase();
    let newQuotes = quotes.filter(i => i.author.toLowerCase().includes(entry));

    let currentIndex;
    for (let i in newQuotes) {
        if (newQuotes[i]['quote'] == currentQuote.textContent) {
            currentIndex = i;
            currentQuote.textContent = newQuotes[parseInt(currentIndex) + 1]['quote'];
            currentAuth.textContent = newQuotes[parseInt(currentIndex) + 1]['author'];
        };
    }
}

function PreviousQuote() {
    let currentQuote = document.getElementById('searchResult');
    let currentAuth = document.getElementById('authorResult');
    let entry = document.getElementById('authorSearch').authorEntry.value.toLowerCase();
    let newQuotes = quotes.filter(i => i.author.toLowerCase().includes(entry));

    let currentIndex;
    for (let i in newQuotes) {
        if (newQuotes[i]['quote'] == currentQuote.textContent) {
            currentIndex = i;
            currentQuote.textContent = newQuotes[parseInt(currentIndex) - 1]['quote'];
            currentAuth.textContent = newQuotes[parseInt(currentIndex) - 1]['author'];
        };
    }
}
