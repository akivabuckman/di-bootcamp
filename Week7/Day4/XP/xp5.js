console.log(document.getElementsByTagName('div')[0])
document.getElementsByClassName('list')[0].lastElementChild.innerText = "Richard";
child = document.getElementsByTagName('ul')[1].children[1];
child.parentElement.removeChild(child)
ulList = document.getElementsByTagName('ul');
console.log(ulList)
for (i of ulList) {
    console.log(i)
    i.firstElementChild.innerText = 'Akiva'
}

for (i of ulList) {
    i.classList.add('student_list')
}

document.getElementsByTagName('ul')[0].classList.add('university', 'attendance')
document.getElementsByTagName('div')[0].setAttribute('style', 'background-color: lightblue')
document.getElementsByTagName('ul')[1].lastElementChild.setAttribute('style', 'display: none')
document.getElementsByTagName('ul')[0].lastElementChild.setAttribute('style', 'border: solid 1px black')
document.body.setAttribute('style', 'font-size: 40px')