const data = require("../xp3data.json")


const Example2 = (props) => {
    return(
        <>
            {data.Skills.map(i=>{
                return(
                    <>
                        <h4>{i.Area}</h4>
                        <ul>
                            {i.SkillSet.map(j=>{
                                return(
                                    <li>{j.Name}</li>
                                )
                            })}
                        </ul>
                    </>
                )
            })}
        
        </>
        
    )
}

export default Example2