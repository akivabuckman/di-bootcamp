//XP1
// Using a DOM property, retrieve the h1 and console.log it.
console.log(document.getElementsByTagName('h1')[0])

// Using DOM methods, remove the last paragraph in the <article> tag.
document.getElementsByTagName('article')[0].lastElementChild.remove()

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
document.getElementsByTagName('h2')[0].addEventListener("click", function() {this.setAttribute('style', 'background-color: red')})

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
document.getElementsByTagName('h3')[0].addEventListener("click", function() {this.setAttribute('style', 'display: none')})

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
let pList = document.getElementsByTagName('p')
newButton = document.createElement('button')
newButton.innerHTML = 'make bold'
newButton.onclick = function () {
    for (let i of pList) {
        i.setAttribute('style', 'font-weight: bold')
    }
}
document.getElementsByTagName('article')[0].appendChild(newButton)

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
document.getElementsByTagName('h1')[0].onmouseover = function () {
    size = Math.floor(Math.random()*100);
    this.setAttribute('style', `font-size: ${parseInt(size)}px`)
}