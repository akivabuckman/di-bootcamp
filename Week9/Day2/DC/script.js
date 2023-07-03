// DC 1

const makeAllCaps = words => {
    return new Promise((resolve, reject) => {
        if (words.every(item => isNaN(item))) {
            resolve(words.map(word => word.toUpperCase()));
        } else {
            reject("you have a non-word in there")
        }
    })
};

const sortWords = words => {
    return new Promise((resolve, reject) => {
        if (words.length > 4) {
            resolve(words.sort())
        } else {
            reject("not enough words")
        }
    })
}

//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, you should see in the console, 
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
      .catch(error => console.log(error));


// DC 2
const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}`


const toJs = (obj) => {
    return new Promise((resolve, reject) => {
        const customObj = JSON.parse(obj);
        if (Object.keys(obj).length !== 0) {
            resolve(customObj);
        } else {
            reject('Object is empty');
        }
    });
};


const toMorse = (morseJS) => {
    userWords = prompt("Enter words: ");
    console.log(userWords);
    return new Promise((resolve, reject) => {
        let morseString = []
        for (let letter of userWords) {
            if (letter == ' ') {
                continue
            } else if (!Object.keys(morseJS).includes(letter)) {
                reject(`${letter} is not a valid character`)
            } else {
                morseString.push(morseJS[letter])
            }
        };
        resolve(morseString);
    })
};

const joinWords = morseTranslation => {
    console.log(morseTranslation);
    for (let i of morseTranslation) {
        let newP = document.createElement('p');
        newP.textContent = i;
        document.body.appendChild(newP);
        newBr = document.createElement('br');
        document.body.appendChild(newBr);
    }
    
};

toJs(morse)
.then(morseJS => toMorse(morseJS))
.then(translation => joinWords(translation));