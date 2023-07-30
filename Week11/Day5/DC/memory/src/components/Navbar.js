const Navbar = (props) => {
    return(
        <nav>
            <h3>Superheroes Memory Game</h3>
            <p>Score: {props.score}</p>
            <p>Top Score: {props.topScore}</p>
        </nav>
    )
}

export default Navbar