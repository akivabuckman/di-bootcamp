let allBooks = [
    {
        'title': 'harry potter',
        'author': 'jk rowling',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Harry_Potter_wordmark.svg/220px-Harry_Potter_wordmark.svg.png',
        'alreadyRead': false
    },
    {
        'title': 'holes',
        'author': 'someone',
        'image': 'https://m.media-amazon.com/images/I/71VJE5yreXS._SL1500_.jpg',
        'alreadyRead': true
    }
]

for (i of allBooks) {
    const bookDiv = document.createElement('div');
    section = document.getElementsByTagName('section')[0];
    section.appendChild(bookDiv);
    let titleP = document.createElement('p');
    titleP.textContent = `${i['title']} written by ${i['author']}`
    bookDiv.appendChild(titleP)
    let bookImage = document.createElement('img');
    bookImage.setAttribute('src', i['image']);
    bookImage.setAttribute('style', 'width: 100px')
    bookDiv.appendChild(bookImage);
    if (i['alreadyRead'] == true) {
        titleP.setAttribute('style', 'color: red')
    }
}