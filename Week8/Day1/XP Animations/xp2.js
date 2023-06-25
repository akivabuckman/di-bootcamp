function myMove() {boxInterval = setInterval(move1, 1)}

i = 0
function move1() {
    document.getElementById('animate').setAttribute('style', `margin-left: ${(i+1).toString()}px`)
    i++;
    if (i==349) {
        clearInterval(boxInterval)
    }
}