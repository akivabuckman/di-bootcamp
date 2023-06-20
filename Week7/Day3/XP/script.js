// XP 1A
const people = ["Greg", "Mary", "Devon", "James"];

people.shift() // removes greg
people.splice(2,1,"Jason") // changes james to jason
people.push("Akiva") // adds to end of array
console.log(people.indexOf("Mary")) // logs index of mary
let copy = people.slice(1,people.length-1) // devon, jason
console.log(people.indexOf("Foo")) // -1 is returned when a value is not found in an array
let last = people[people.length-1] // akiva

// XP 1B
for (i of people) {
    console.log(i)
}

for (i of people) {
    console.log(i);
    if (i == "Devon") {
        break
    }
}

// XP 2
console.log("\nXP2")
const colors = ["red", "orange", "yellow", "green", "blue"]
const suffixes = ["st", "nd", "rd", "th", "th"]
for (let i in colors) {
    console.log(`My ${parseInt(i)+1}${suffixes[i]} favorite color is ${colors[i]}`)
}

// XP 3
// let valid = false
// do {
//     let num = parseFloat(prompt("Give a number under 10"));
//     if (num > 10) {
//         valid = true
//     }
// }
// while (valid == false);

// XP 4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log(building['numberOfFloors'])
const first = parseInt(building['numberOfAptByFloor']['firstFloor']);
const third = parseInt(building['numberOfAptByFloor']['thirdFloor']);
console.log(first + third)
console.log(building.nameOfTenants[1])
console.log(building.numberOfRoomsAndRent.dan[0])
const sarahRent = building.numberOfRoomsAndRent.sarah[1]
const davidRent = building.numberOfRoomsAndRent.david[1]
let danRent = building.numberOfRoomsAndRent.dan[1]
if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200
}

// XP 5
// Create an object called family with a few key value pairs.
let family = {
    size: 5,
    name: 'buckman'
}

// Using a for in loop, console.log the keys of the object.
for (let i in family) {
    console.log(i)
}

// Using a for in loop, console.log the values of the object.
for (let i in family) {
    console.log(family[i])
}

// XP 6
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”
// btw it's reindeer, not raindeer.
for (let i in details) {
    console.log(i);
    console.log(details[i])
}

// XP 7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort()
let a = ""
for (let i of names) {
    a += i[0]
}
console.log(a)