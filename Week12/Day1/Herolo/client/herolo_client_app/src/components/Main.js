

const Main = () => {

    const cityComplete = async (e) => {
        if (e.target.value.length > 2) {
            console.log(e.target.value)
        }
    }

    return(
        <>
            <form>
                <label htmlFor="cityInput">Enter City:</label>
                <input onChange={cityComplete} type="text" id="cityInput" placeholder="Enter City..."></input>
            </form>
        
        </>
        
    )
}

export default Main