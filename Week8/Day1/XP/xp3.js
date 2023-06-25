// Declare a global variable named allBoldItems.
let allBoldItems = []

// Create a function called getBoldItems() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.
function getBoldItems() {
    for (i of document.getElementsByTagName('strong')) {
        allBoldItems.push(i)
    }
    return allBoldItems
}

// Create a function called highlight() that changes the color of all the bold text to blue.
function highlight() {
    for (let i of getBoldItems()) {
        i.setAttribute('style', 'color: blue')
    }
}

// Create a function called returnItemsToDefault() that changes the color of all the bold text back to black.
function returnItemsToDefault() {
    for (let i of getBoldItems()) {
        i.setAttribute('style', 'color: black')
    }
}
// Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function returnItemsToDefault() on mouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example
document.getElementsByTagName('p')[0].onmouseover = highlight;
document.getElementsByTagName('p')[0].onmouseout = returnItemsToDefault;







