function hello() {
    alert('Hello World')
}

// setTimeout(hello, 2000)

function addP () {
    newP = document.createElement('p')
    newP.textContent = 'Hello World'
    document.getElementById('container').appendChild(newP)
    pCount = document.getElementsByTagName('p').length

    if (pCount >=5) {
        clearInterval(pInt)
    }
    console.log(pCount)

}

// setTimeout(addP, 2000)

let pInt = setInterval(addP, 2000) // creates new p every 2 seconds

document.getElementById('clear').onclick = function() {clearInterval(pInt)}