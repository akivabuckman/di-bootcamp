import logo from './logo.svg';
import './App.css';
import Navbar from './components/Navbar';
import Cards from './components/Cards';
import {useState, useEffect} from "react";

function App() {
  const [score, setScore] = useState(0);
  const [topScore, setTopScore] = useState(0);

  return (
    <>
      <div id="navDiv">
        <Navbar score={score} topScore={topScore} setScore={setScore} setTopScore={setTopScore}/>
      </div>

      <div id="cardsDiv">
      <Cards score={score} topScore={topScore} setScore={setScore} setTopScore={setTopScore}/>

      </div>
    
    </>
  

  );
}

export default App;
