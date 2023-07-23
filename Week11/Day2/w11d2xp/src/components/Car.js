import React from 'react';
import { useState, useEffect } from "react";
import Garage from './Garage';


const Car = ({instance}) => {
    // <h1>This car is {instance.model}</h1> // part 1

    const [color, setColor] = useState("turquoise");

    return <>
    <h1>This car is a {color} {instance.model}</h1>
    <Garage size="medium" />
    </>
    
}

export default Car