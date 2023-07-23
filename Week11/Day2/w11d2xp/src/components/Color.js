import React from 'react';
import { useState, useEffect } from "react";

const Color = () => {
    const [favoriteColor, setFavoriteColor] = useState("red")

    const changeColor = () => {
        setFavoriteColor("blue")
    }

    useEffect(()=>{
        alert(`useEffect reached - color changed to ${favoriteColor}`)
    }, [favoriteColor])
    
    return(
        <>
        <h1>My Favorite Color is {favoriteColor}</h1>
        <button onClick={changeColor}>Change Color</button>
        </>
    )
};

export default Color