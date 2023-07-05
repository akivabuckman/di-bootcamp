// XP1
// Create a program to retrieve the data from the API URL provided above.
// Use the fetch() method to make a GET request to the Giphy API and Console.log the Javascript Object that you receive.
// Make sure to check the status of the Response and to catch any occuring errors.

const url = "https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"

const getGif = () => {
    fetch(url)
        .then(response => {
            console.log(response);
            if(response.ok === true) {
                return response.json()
            } else {
                throw new Error("bad gif data")
            }
        })
        .then(jsonResponse => {
            console.log(jsonResponse);
        })
        .catch(error => {
            console.log(error);
        });
};

// getGif()

// XP2
// Read carefully the documention to understand all the possible queries that the URL accept.
// Use the Fetch API to retrieve 10 gifs about the “sun”. The starting position of the results should be 2.
// Make sure to check the status of the Response and to catch any occuring errors.
// Console.log the Javascript Object that you receive.

const sunUrl = "https://api.giphy.com/v1/gifs/search?q=sun&limit=20&offset=2&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
const getSunGif = () => {
    fetch(sunUrl)
        .then(response => {
            console.log(response);
            if(response.ok === true) {
                return response.json()
            } else {
                throw new Error("bad gif data")
            }
        })
        .then(jsonResponse => {
            console.log(jsonResponse);
        })
        .catch(error => {
            console.log(error);
        });
};

// XP3
// Create an async function, that will await for the above GET request.
// The program shouldn’t contain any then() method.
// fetch("https://www.swapi.tech/api/starships/9/")
//     .then(response => response.json())
//     .then(objectStarWars => console.log(objectStarWars.result));

const spaceFetch = async endpoint => {
    try {
        const response = await fetch(endpoint);
        if (response.status == 400) {
            throw new Error('darth vader is messing with us');
        } else {
            let data = await response.json();
            let objectStarWars = data.result;
            console.log(objectStarWars)
        }
    } catch (error) {
        console.log(`darth vader says ${error}`)
    }
};

// spaceFetch("https://www.swapi.tech/api/starships/9/")

// XP4
function resolveAfter2Seconds() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve('resolved');
        }, 2000);
    });
}

async function asyncCall() {
    console.log('calling');
    let result = await resolveAfter2Seconds();
    console.log(result);
}

asyncCall();

// calling
// resolved