function anagram(word1, word2) {
    // get letters into an array, without spaces
    let word1Letters = [...word1.replace(/\s/g, "")].map((letter, index, arr) => {
        if (letter != ' ') {
            return letter
        } 
    });
    let word2Letters = [...word2.replace(/\s/g, "")].map((letter, index, arr) => {
        if (letter != ' ') {
            return letter
        } 
    });

    // make object of each letter and it's count, for each word
    let letterCount1 = {};
    for (let i of word1Letters) {
        letterCount1[i] = word1Letters.filter((j) => (j === i)).length;
    };
    
    let letterCount2 = {};
    for (let i of word1Letters) {
        letterCount2[i] = word2Letters.filter((j) => (j === i)).length;
    };

    // if any count of any letter is different, semiMatch is false.
    let semiMatch = true
    for (let letter of word1Letters) {
        if (letterCount1[letter] != letterCount2[letter]) {
            semiMatch = false
        }
    };
    
    // check length to make sure word2 has no letters that word1 doesnt
    return semiMatch && word1Letters.length == word2Letters.length ? true : false;
};
