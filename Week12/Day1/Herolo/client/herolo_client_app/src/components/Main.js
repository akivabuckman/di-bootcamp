import apikey from "../apikey/apikey.js"
import {useState, useEffect} from "react";

const Main = () => {
    const [cityKey, setCityKey] = useState(215854);
    const [cityName, setCityName] = useState("Tel Aviv")
    const [weatherText, setWeatherText] = useState(null);
    const [temp, setTemp] = useState(null);
    const [forecast, setForecast] = useState([]);
    const [favorites, setFavorites] = useState([]);


    const cityComplete = async (e) => {
        if (e.target.value.length > 2) {
            try {
                const cityUrl = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete"
                const response = await fetch(`${cityUrl}?apikey=${apikey}&q=${e.target.value}`);
                const data = await response.json();
                setCityKey(data[0].Key);
                setCityName(data[0].LocalizedName)
                console.log("city: ", data[0].LocalizedName)
            } catch(error) {
                console.log(error)
            }  
        }
    }

    const displayCurrent = async () => {
        try {
            const currentUrl = "http://dataservice.accuweather.com/currentconditions/v1/";
            const response = await fetch(`${currentUrl}${cityKey}?apikey=${apikey}&details=false`);
            const data = await response.json();
            setWeatherText(data[0].WeatherText);
            setTemp(data[0].Temperature.Metric.Value);
            
        } catch (error) {
            console.log(error)
        }
    }

    const displayForecast = async () => {
        const localForecast = [];
        try {
            const forecastUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/";
            const response = await fetch (`${forecastUrl}${cityKey}/?apikey=${apikey}&metric=true`);
            const data = await response.json();
            for (let i of data.DailyForecasts) {
                let day = {
                    "date": i.Date,
                    "daytime": {
                        "temperature": i.Temperature.Maximum.Value,
                        "iconPhrase": i.Day.IconPhrase
                    },
                    "night": {
                        "temperature": i.Temperature.Minimum.Value,
                        "iconPhrase": i.Night.IconPhrase
                    }
                };
                localForecast.push(day)
            };
            setForecast(localForecast)
            console.log(forecast);

        } catch(error) {
            console.log(error)
        }
    }

    const addToFavorites = () => {
        setFavorites([{cityKey: cityName}, ...favorites]);
        console.log(favorites)
    };

    const removeFromFavorites = () => {
        setFavorites((current) =>
          current.filter((city) => city !== cityName)
        );
        console.log("favorites", favorites)
    };

    useEffect(()=>{
        displayCurrent();
        displayForecast();
    }, [cityKey])

    return(
        <>
            <form>
                <label htmlFor="cityInput">Enter City:</label>
                <input onChange={cityComplete} type="text" id="cityInput" placeholder="Enter City..."></input>
            </form>
            <div id="currentWeather">
                {Object.keys(favorites).includes(cityKey) ? 
                    <button onClick={removeFromFavorites}>Remove {cityName} from Favorites</button> :
                    <button onClick={addToFavorites}>Add {cityName} to Favorites</button>}
                <h3>Current Weather for {cityName}:</h3>
                <p>Conditions: {weatherText}</p>
                <p>Temperature: {temp}</p>
            </div>
            <div id="forecast">
                <h3>5-Day Forecast:</h3>
                {
                    forecast.map(i=>{
                        return(
                            <div class="day">
                                <strong>Date: {i.date.slice(0,10)}</strong>
                                <p>Day: {i.daytime.iconPhrase}, {i.daytime.temperature}C</p>
                                <p>Night: {i.night.iconPhrase}, {i.night.temperature}C</p>
                                <hr/>
                            </div>
                        )
                        
                    })
                }
            </div>
        
        </>
    )
}

export default Main