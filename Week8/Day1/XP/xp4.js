//XP4
button = document.getElementById('submit')
button.onclick = calculate

function calculate(e) {
    let radius = parseFloat(document.getElementById('radius').value);
    let volume = radius ** 3 * Math.PI * 4 / 3;
    document.getElementById('volume').value = volume;
    e.preventDefault()
}

//XP5
let radiusLabel = document.getElementsByTagName('form')[0].firstElementChild;
radiusLabel.addEventListener("click", function() {this.setAttribute('style', 'background-color:red')})
radiusLabel.addEventListener("dblclick", function() {this.setAttribute('style', 'background-color:blue')})
radiusLabel.addEventListener("mouseover", function() {this.setAttribute('style', 'color:turquoise')})
radiusLabel.addEventListener("mouseout", function() {this.setAttribute('style', 'color:orange')})