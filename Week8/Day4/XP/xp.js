// XP1
// Analyze the code below. What will be the output?

const person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}

const {name, location: {country, city, coordinates: [lat, lng]}} = person;

console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);
// I am John Doe from Vancouver, Canada. Latitude(49.287), Longitude(-123.1207)

// XP2
function displayStudentInfo(objUser){
    const {first, last} = objUser;
    console.log(`Your full name is ${first} ${last}`)
}

displayStudentInfo({first: 'Elie', last:'Schoppik'});


// Using the code above, destructure the parameter inside the function and return a string as the example seen below:
//output : 'Your full name is Elie Schoppik'

// XP3

// Using this object 
const users = { user1: 18273, user2: 92833, user3: 90315 };

// Using methods taught in class, turn the users object into an array:
// Excepted output: [ [ 'user1', 18273 ], [ 'user2', 92833 ], [ 'user3', 90315 ] ]
// FYI : The number is their ID number.
const usersArray = Object.entries(users);

// Modify the outcome of part 1, by multipling the user’s ID by 2.
// Excepted output: [ [ 'user1', 36546 ], [ 'user2', 185666 ], [ 'user3', 180630 ] ]
usersArray.forEach((vals, i, arr) => {
     arr[i] = [vals[0], vals[1] * 2];
});

// XP4
// Analyze the code below. What will be the output?
class Person {
  constructor(name) {
    this.name = name;
  }
}

const member = new Person('John');
console.log(typeof member);
// object

// XP5
// Using the Dog class below:

class Dog {
  constructor(dogname) {
    this.dogname = dogname;
  }
};
// Analyze the options below. Which constructor will successfully extend the Dog class?
  // 1
// class Labrador extends Dog {
//   constructor(dogname, size) {
//     this.size = size;
//   }
// };


  // 2
class Labrador extends Dog {
  constructor(dogname, size) {
    super(dogname);
    this.size = size;
  }
};


//   // 3
// class Labrador extends Dog {
//   constructor(size) {
//     super(dogname);
//     this.size = size;
//   }
// };


//   // 4
// class Labrador extends Dog {
//   constructor(dogname, size) {
//     this.dogname = dogname;
//     this.size = size;
//   }
// };

// 2 is correct


// XP6
// Evaluate these (ie True or False)

[2] === [2]; //true
// {} === {}; //error


// What is, for each object below, the value of the property number and why?

const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
console.log(object2.number) // 4 because object1 and object2 share the same data address. when one is changed the other is also.
console.log(object3.number) // 4 for the same reason
console.log(object4.number) // 5 because it was defined as 5 and never changed to anything elsse


// Create a class Animal with the attributes name, type and color. The type is the animal type, for example: dog, cat, dolphin ect …
class Animal {
    constructor(animalName, type, color) {
        this.animalName = animalName;
        this.type = type;
        this.color = color
    }
}
// Create a class Mamal that extends from the Animal class. Inside the class, add a method called sound(). This method takes a parameter: the sound the animal makes, and returns the details of the animal (name, type and color) as well as the sound it makes.
class Mammal extends Animal {
    sound(animalSound) {
        this.animalSound = animalSound
        console.log(`${this.animalSound} I'm a ${this.type}, named ${this.animalName} and I'm ${this.color}`)
        return {
            "name": this.animalName,
            "type": this.type,
            "color": this.color,
            "sound": this.animalSound
        }
    }
};

// Create a farmerCow object that is an instance of the class Mamal. The object accepts a name, a type and a color and calls the sound method that “moos” her information.
// For example: Moooo I'm a cow, named Lily and I'm brown and white
let farmerCow = new Mammal(animalName='Lily', type='cow', color='brown and white', animalSound='Moooo');
farmerCow.sound('Moooo');