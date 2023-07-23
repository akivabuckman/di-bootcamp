import React from 'react';
import { useState, useEffect } from "react";

const Events = () => {
    const [IsToggleOn, setIsToggleOn] = useState("true")

    const ClickMe = () => {
        alert("I ws clicked");
    };

    const handleKeyDown = (event) => {
        if (event.keyCode === 13) {
            alert(`Enter key was pressed. input is "${document.querySelector("#input").value}"`)
        }
    }

    const toggle = () => {
        setIsToggleOn(IsToggleOn ? false : true)
    }
    
    return(
        <>
        <button onClick={ClickMe}>Click here</button>
        <br></br>
        <input id="input" onKeyDown={handleKeyDown} placeholder='Press the ENTER key!'></input>
        <br></br>
        <button onClick={toggle}>{IsToggleOn ? "ON" : "OFF"}</button>
        </>
    )
};



export default Events;