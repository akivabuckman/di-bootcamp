let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

// Create an arrow function named displayGroceries, that console.logs the 3 fruits from the groceries object. Use the forEach method.
const displayGroceries = (obj) => obj.fruits.forEach((fruit) => {console.log(fruit)})

// Create another arrow function named cloneGroceries.
// In the function, create a variable named user that is a copy of the client variable. (Tip : make the user variable equal to the client variable)
// const cloneGroceries = () => user = client

// Change the client variable to “Betty”. Will we also see this modification in the user variable ? Why ?
client = 'Betty' // the user variable will still be "John" because the 'user' and 'client' variables have different data addresses

// In the function, create a variable named shopping that is equal to the groceries variable.
const cloneGroceries = () => shopping = groceries; groceries.totalPrice = "35$"; groceries.other.payed = false;
// Change the value of the totalPrice key to 35$. Will we also see this modification in the shopping object ? Why ?
cloneGroceries()

// shopping.totalPrice will also be "35$" because groceries and shopping share the same data address. they are the same exact object.

// Change the value of the payed key to false. Will we also see this modification in the shopping object ? Why ?

// yes shopping will also be false because groceries and shopping share the same data address. they are the same exact object.
// Invoke the cloneGroceries function.