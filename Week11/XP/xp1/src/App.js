import React from "react";
import UserFavoriteAnimals from "./components/FavoriteAnimals.component"
import Exercise from "./components/Exercise3"
import './style.css'

export function App1() {
  // const myElement = <h1>Hello World!</h1>; part 1
  const sum = 5 + 5;
  const myElement = <h1>React is {sum} times better with JSX</h1>
  return myElement 
};

export function App2() {
  const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals: ["Horse", "Turtle", "Elephant", "Monkey"]
  };

  const output = 
  <>
  <h3>{user.firstName}</h3>
  <h3>{user.lastName}</h3>
  <UserFavoriteAnimals favorites={user.favAnimals}/>
  </>
  return output
};

export function App3() {
  const output = <Exercise />
  return output
}