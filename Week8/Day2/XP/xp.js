// XP1
// 1.1 a will equal 3
// 1.2 error - const cannot be reassigned
// 2.1 
// funcThree() 'inside the funcThree function 0'
// funcTwo()
// funcThree() 'inside the funcThree function 5'
// 2.2
// error because a const cant be reassigned
// 3.1
// funcFour() 
// funcFive() 'inside the funcFive function hello'
// 4.1
// funcSix() 'inside the funcSix function test
// 4.2 error because a const cant be reassigned
// 5.1 'in the if block 5' , then another alert 'outside of the if block 2'
// 5.2 it still works because it's being assigned in separate "places"

// XP2
// Transform the winBattle() function to an arrow function.
const winBattle = () => true;

// Create a variable called experiencePoints.
let experiencePoints

// Assign to this variable, a ternary operator. If winBattle() is true, the experiencePoints variable should be equal to 10, else the variable should be equal to 1.
experiencePoints = winBattle ? 10 : 1

// Console.log the experiencePoints variable.
console.log(experiencePoints)

// XP3
// Write a JavaScript arrow function that checks whether the value of the argument passed, is a string or not. The function should return true or false
const isString = givenString => typeof givenString === 'string' ? true : false

// XP4
// Create a one line function (ie. an arrow function) that receives two numbers as parameters and returns the sum.
const sumGetter = (a, b) => a + b

//XP5
// Create a function that receives a weight in kilograms and returns it in grams. (Hint: 1 kg is 1000gr)
// First, use function declaration and invoke it.
function convert1(kg) {
    return kg * 1000
}
convert1(2)

// Then, use function expression and invoke it.
let convert2 = function(kg) {
    return kg * 1000
}
convert2(2)

// Write in a one line comment, the difference between function declaration and function expression.
// in function expression, the function is assigned to a variable. Function declarations are hoisted, expressions are not.


// Finally, use a one line arrow function and invoke it.
const convert3 = kg => kg * 1000;
convert3(2);

// XP6
(function (childrenCount, partner, location, job) {
    newP = document.createElement('p');
    newP.textContent = `You will be a ${job} in ${location}, and married to ${partner} with ${childrenCount} kids.`
    document.body.appendChild(newP)
}) (3, 'liat', 'israel', 'engineer');

// XP7
// John has just signed in to your website and you want to welcome him.
// Create a Navbar in your HTML file.
// In your js file, create a self invoking funtion that takes 1 argument: the name of the user that just signed in.
// The function should add a div in the nabvar, displaying the name of the user and his profile picture.
(function (name) {
    let newDiv = document.createElement('div');
    let newP = document.createElement('p');
    newP.textContent = `hello ${name}`;
    newDiv.appendChild(newP);
    document.getElementsByTagName('nav')[0].appendChild(newDiv);
    let newImg = document.createElement('img');
    newImg.setAttribute('src', 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/John_Legend_2019_by_Glenn_Francis.jpg/220px-John_Legend_2019_by_Glenn_Francis.jpg')
    newDiv.appendChild(newImg)

})('John Legend')

// XP8
//Part I
function makeJuice(size) {
    function addIngredients(firstIng, secondIng, thirdIng) {
        newP = document.createElement('p');
        newP.textContent = `The client wants a ${size} juice, containing ${firstIng}, ${secondIng}, and ${thirdIng}`;
        document.body.appendChild(newP);
    }
    addIngredients('apple', 'banana', 'canteloupe')
}
makeJuice('medium')

// Part II
function makeJuice2(size) {
    let ingredients = [];
    function addIngredients(firstIng, secondIng, thirdIng) {
        ingredients.push(firstIng, secondIng, thirdIng);
    }
    function displayJuice(ingredients) {
        newP = document.createElement('p');
        endText = ""
        for (i of ingredients) {
            endText += `${i}, `
        }
        newP.textContent = `The client wants a ${size} juice, containing ${endText.slice(0,-2)}`;
        document.body.appendChild(newP);
    }
    addIngredients('apple', 'banana', 'canteloupe');
    addIngredients('pear', 'peach', 'grapes');
    console.log(ingredients)
    displayJuice(ingredients)
}
makeJuice2('large')