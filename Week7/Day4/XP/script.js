//XP1
function displayNumbersDivisible(divisor) {
    let sum = 0;
    let listnums = "";
    for (i=0; i<= 500; i++) {
        if (i % divisor == 0) {
            listnums += `${i.toString()} `
            sum += i
        }
    }
    console.log(listnums)
    console.log(`Sum: ${sum}`)
}

displayNumbersDivisible(24)

//XP2
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ['banana', 'orange', 'apple'];

function myBill() {
    let total = 0;
    for (i of shoppingList) {
        if (stock[i] > 0) {
            total += prices[i];
            stock[i] -= 1
        }
    }
    console.log(total)
    console.log(stock)
}

myBill()

//XP3
function changeEnough(itemPrice, amountOfChange) {
    const balance = .25 * amountOfChange[0] + .1 * amountOfChange[1] + .05 * amountOfChange[2] + .01 * amountOfChange[3];
    console.log(balance)
    console.log(itemPrice)
    return (balance < itemPrice ? false : true)
}

//XP4
function hotelCost() {
    do {
        var nights = parseInt(prompt("how many nights?"))
    }
    while (isNaN(nights))
    return (nights * 140)
}

function planeRideCost() {
    while (true) {
        var dest = prompt("destination?");
        if (dest && isNaN(dest)) {
            if (dest == 'London') {
                return 183
            } else if (dest == 'Paris') {
                return 220
            } else {
                return 300
            }
        }
    }
}

rentalCarCost() {
    do {
        var nights = parseInt(prompt("how many nights?"))
    }
    while (isNaN(nights))
}

