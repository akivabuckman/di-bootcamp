const robots = [
    {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      image: 'https://robohash.org/1?200x200'
    },
    {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      image: 'https://robohash.org/2?200x200'
    },
    {
      id: 3,
      name: 'Clementine Bauch',
      username: 'Samantha',
      email: 'Nathan@yesenia.net',
      image: 'https://robohash.org/3?200x200'
    },
    {
      id: 4,
      name: 'Patricia Lebsack',
      username: 'Karianne',
      email: 'Julianne.OConner@kory.org',
      image: 'https://robohash.org/4?200x200'
    },
    {
      id: 5,
      name: 'Chelsey Dietrich',
      username: 'Kamren',
      email: 'Lucio_Hettinger@annie.ca',
      image: 'https://robohash.org/5?200x200'
    },
    {
      id: 6,
      name: 'Mrs. Dennis Schulist',
      username: 'Leopoldo_Corkery',
      email: 'Karley_Dach@jasper.info',
      image: 'https://robohash.org/6?200x200'
    },
    {
      id: 7,
      name: 'Kurtis Weissnat',
      username: 'Elwyn.Skiles',
      email: 'Telly.Hoeger@billy.biz',
      image: 'https://robohash.org/7?200x200'
    },
    {
      id: 8,
      name: 'Nicholas Runolfsdottir V',
      username: 'Maxime_Nienow',
      email: 'Sherwood@rosamond.me',
      image: 'https://robohash.org/8?200x200'
    },
    {
      id: 9,
      name: 'Glenna Reichert',
      username: 'Delphine',
      email: 'Chaim_McDermott@dana.io',
      image:'https://robohash.org/9?200x200'
    },
    {
      id: 10,
      name: 'Clementina DuBuque',
      username: 'Moriah.Stanton',
      email: 'Rey.Padberg@karina.biz',
      image:'https://robohash.org/10?200x200'
    }
];

function displayRobots(relevantRobots) {
    let parent = document.getElementById('card-container');
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild)
    }
    for (let robot of relevantRobots) {
        let newDiv = document.createElement('div');
        newDiv.setAttribute('class', 'card');
        parent.appendChild(newDiv);

        let newImg = document.createElement('img');
        newImg.setAttribute('src', robot.image);
        newDiv.appendChild(newImg)

        let newH2 = document.createElement('h2');
        newH2.setAttribute('class', 'robot-name');
        newH2.textContent = robot.name;
        newDiv.appendChild(newH2);

        let newH3 = document.createElement('h3');
        newH3.setAttribute('class', 'email');
        newH3.textContent = robot.email;
        newDiv.appendChild(newH3);
    }
}

// initialization of the webpage upon load
displayRobots(robots);

// what happens when search occurs:
document.getElementById('button').addEventListener("click", filterResults);
function filterResults() {
    let entry = document.getElementById('searchEntry').value.toLowerCase();
    if (entry != '') {
        let newRobots = robots.filter(robot => robot.name.toLowerCase().includes(entry));
        displayRobots(newRobots);
    } else {
        displayRobots(robots);
    }
}