import {useState, useEffect} from "react";
import apikey from "../apikey/apikey.js"
const express = require('express');
const app = express();
const cors = require("cors");
app.use(cors())


const Favorites = () => {
    const [favorites, setFavorites] = useState([
        {"215854": "tel aviv"},
        {"111111": "cleveland"}
    ])
    const [currents, setCurrents] = useState([])
    const displayCurrents = async () => {
        for (let i of favorites) {
            console.log("i", i)
            try {
                const currentUrl = "http://dataservice.accuweather.com/currentconditions/v1/";
                const response = await fetch(`${currentUrl}${Object.keys(i)[0]}?apikey=${apikey}&details=false`);
                const data = await response.json();
                const weatherText = data[0].WeatherText;
                const temp = data[0].Temperature.Metric.Value;
                const cityKey = Object.keys(i)[0];
                const cityName = Object.values(i)[0];
                const j = {
                    [cityName]: {
                        weatherText,
                        temp,
                        cityKey,
                        cityName
                    }
                }
                setCurrents(prevCurrents => [j, ...prevCurrents]); 
                console.log("jcur", currents)
            } catch(error) {
                console.log(error)
            }
        };
        setTimeout(() => {
            console.log("currents", currents)
        }, 2000);
        
    }


    useEffect(()=>{
        displayCurrents()
    }, [favorites])

    return(

        <div id="favorites">
            <h1>Favorite Places:</h1>
            {
                currents.map(i=>{
                    return (
                        <>
                        <h3>{Object.keys(i)[0]}</h3>
                        </>
                        
                    )
                })
            }

        </div>
    )
}

export default Favorites