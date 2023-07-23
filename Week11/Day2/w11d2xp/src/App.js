import React from "react";
import Car from "./components/Car";
import Events from "./components/Events";
import Phone from "./components/Phone";
import Color from "./components/Color";

const carinfo = {name: "Ford", model: "Mustang"};

export function App1() {
  const output = <Car instance = {carinfo} />;
  return output
}

export function App2() {
  const output = <Events />
  return output
}

export function App3() {
  const output = <Phone />
  return output
}

export function App4() {
  return <Color />
}

export default App3