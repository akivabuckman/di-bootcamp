import logo from './logo.svg';
import './App.css';
import quotes from "./quotes"
import {useState, useEffect} from "react";






const App = () => {
  const firstIndex = Math.floor(Math.random()*quotes.length)
  const [color, setColor] = useState("rgb(111, 255, 255)")
  const [quoteIndex, setQuoteIndex] = useState(firstIndex)


  const changeIndex = () => {
    const newIndex = Math.floor(Math.random()*quotes.length)
    console.log(newIndex)
    console.log(quotes)
    console.log(quotes[newIndex])
    console.log("len", quotes.length)
    setQuoteIndex(newIndex)
    quotes.splice(quoteIndex, 1)
  }

  const changeColor = () => {
    const r = Math.floor(Math.random()*255)
    const g = Math.floor(Math.random()*255)
    const b = Math.floor(Math.random()*255)
    setColor(`rgb(${r}, ${g}, ${b})`)
  }

  useEffect(()=>{
    changeColor()
  }, [quoteIndex])

  return (
    <div style={{backgroundColor: color, height:"100vh"}} className="App" id="colorDiv">
      <div id="whiteDiv" style={{backgroundColor: "white"}}>
        <h3 style={{color: color}}>{quotes[quoteIndex]["quote"]}</h3>
        <h5 style={{color: color}}>-{quotes[quoteIndex]["author"]}-</h5>
        <button onClick={changeIndex} style={{backgroundColor: color}}>Get Quote</button>
      </div>
     

    </div>
  );
}

export default App;
