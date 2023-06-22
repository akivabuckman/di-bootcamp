const planets = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']
const moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 95,
    'saturn': 146,
    'uranus': 27,
    'neptune': 14,
}

var parentElement = document.getElementsByTagName('section')[0];
for (i in planets) {
    const planetDiv = document.createElement('div');
    planetDiv.classList.add('planet');
    planetDiv.classList.add(planets[i]);
    parentElement.appendChild(planetDiv);
}

for (i of planets) {
    const parentPlanet = document.getElementsByClassName(i)[0];
    for (var j = 0; j < moons[i]; j++) {
        const moonDiv = document.createElement('div');
        moonDiv.className = 'moon';
        console.log(parentPlanet)
        parentPlanet.appendChild(moonDiv);
    }
}