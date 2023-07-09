const nameElement = document.querySelector("#name");
const heightElement = document.querySelector("#height");
const genderElement = document.querySelector("#gender");
const birth_yearElement = document.querySelector("#birth_year");
const homeworldElement = document.querySelector("#homeworld");
    
async function getUserData(id) {
    const url = `https://www.swapi.tech/api/people/${id}`;
    try {
        for (i of [nameElement, heightElement, genderElement, birth_yearElement, homeworldElement]) {
            i.classList.remove('hidden');
            i.classList.add('shown');
        }
        const response = await fetch(url);
        const resJson = await response.json();
        const {name, height, gender, birth_year, homeworld} = resJson.result.properties; 
        const homeworldName = await fetchHomeworld(homeworld);
        displayProperties(name, height, gender, birth_year, homeworldName);
    } catch (error) {
        document.querySelector("#error").classList.add('shown');
        document.querySelector("#error").classList.remove('hidden');
        for (i of [nameElement, heightElement, genderElement, birth_yearElement, homeworldElement]) {
            i.classList.add('hidden');
            i.classList.remove('shown');
        }
    }
};

function displayProperties(name, height, gender, birth_year, homeworld) {
    document.querySelector("#error").classList.remove('shown');
    document.querySelector("#error").classList.add('hidden');

    nameElement.textContent = "Name: " + name;
    heightElement.textContent = "Height: " + height;
    genderElement.textContent = "Gender: " + gender;
    birth_yearElement.textContent = "Birth Year: " + birth_year;
    homeworldElement.textContent = "Homeworld: " + homeworld;
}

async function fetchHomeworld(homeworld) {
    
    try {
        const res = await fetch(homeworld);
        const resJson = await res.json();
        const homeworldName = resJson.result.properties.name;
        return homeworldName;
    } catch (error) {
        console.error(error);
    }
}

document.querySelector("#button").addEventListener("click", handleClick)

function handleClick(e) {
    const MAXNUM = 160;
    const randomId = Math.floor(Math.random() * MAXNUM + 1);
    getUserData(randomId);
}   
