import SuperHeroes from "./SuperHeroes";
import {useState, useEffect} from "react";


const shuffleArray = () => {
    const numbers = Array.from({ length: 12 }, (_, index) => index + 1)
    for (let i = numbers.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
    }
    return numbers
}


const Cards = (props) => {
    const [order, setOrder] = useState(shuffleArray())
    const [clicked, setClicked] = useState([])

    const handleclick = async (e) => {
        if (clicked.includes(e.target.id)) {
            props.setScore(0)
            setClicked([]);
        } else {
            props.setScore(props.score + 1)
            if (props.score >= props.topScore) {
                props.setTopScore(props.score + 1 )
            };
            console.log(e.target.id)
            await setClicked([e.target.id, ...clicked])
        }
        setOrder(shuffleArray())
    }

    useEffect(()=>{
        console.log(clicked)
    })
      
    return(
        <>
            {
            order.map(i=> (
                <div id={SuperHeroes.superheroes.filter(hero=>hero.id===i)[0]["id"]} onClick={handleclick} class="card">
                    <img id={SuperHeroes.superheroes.filter(hero=>hero.id===i)[0]["id"]} alt={SuperHeroes.superheroes.filter(hero=>hero.id===i)[0]["name"]} src={SuperHeroes.superheroes.filter(hero=>hero.id===i)[0]["image"]}></img>
                    <p id={SuperHeroes.superheroes.filter(hero=>hero.id===i)[0]["id"]}><strong>Name: </strong>{SuperHeroes.superheroes.filter(hero=>hero.id===i)[0]["name"]}</p>
                    <p id={SuperHeroes.superheroes.filter(hero=>hero.id===i)[0]["id"]}><strong>Occupation: </strong>{SuperHeroes.superheroes.filter(hero=>hero.id===i)[0]["occupation"]}</p>
                </div>
                )) 
            }
        </> 
    )
}

export default Cards