const data = require("../xp3data.json")


const Example3 = (props) => {
    return (
        <>
        {
            data.Experiences.map(i=>{
                return(
                    <div>
                        <img src={i.logo} alt={i.companyName}></img>
                        <br></br>
                        <a href={i.url}>{i.companyName}</a>
                        {
                            i.roles.map(j=>{
                                return(
                                    <div>
                                        <p><strong>{j.title}</strong></p>
                                        <p>{j.startDate} <span>{j.location}</span></p>
                                        <p>{j.description}</p>
                                    </div>
                                )
                            })
                        }
                    </div>
                )
            })
        }
        </>
    )
}

export default Example3