const data = require("../xp3data.json")


const Example1 = (props) => {
    return(
        <ul>
            {data.SocialMedias.map(i=>{
                return(
                    <li>{i}</li>
                )
            })}
        </ul>
    )
}

export default Example1