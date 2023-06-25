// Retrieve the form and console.log it.
console.log(document.getElementsByTagName('form')[0])

// Retrieve the inputs by their id and console.log them.
console.log(document.getElementById('fname'))
console.log(document.getElementById('lname'))

// Retrieve the inputs by their name attribute and console.log them.
console.log(document.getElementsByName('fname'))
console.log(document.getElementsByName('lname'))

document.getElementById('submit').addEventListener("click", submitFunc)

function submitFunc(e) {
    e.preventDefault(); // to prevent the page from reloading upon click
    let givenFName = document.getElementById('fname').value;
    let givenLName = document.getElementById('lname').value;
    for (let i of [givenFName, givenLName]) {
        if (givenFName != '' && givenLName != '') {
            newLi = document.createElement('li');
            newLi.textContent = i;
            document.getElementsByClassName('usersAnswer')[0].appendChild(newLi)
        }
    }
}
// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
// The output should be :

// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>