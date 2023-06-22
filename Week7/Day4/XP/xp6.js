document.getElementById('navBar').setAttribute('id', 'socialNetworkNavigation');
var newLi = document.createElement('li');
let newText = document.createTextNode('Logout');
newLi.appendChild(newText);
document.getElementsByTagName('ul')[0].appendChild(newLi);
firstText = document.getElementsByTagName('ul')[0].firstElementChild.textContent
lastText = document.getElementsByTagName('ul')[1].lastElementChild.textContent