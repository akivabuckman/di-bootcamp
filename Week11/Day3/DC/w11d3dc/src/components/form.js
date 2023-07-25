import {useState, useEffect} from "react";

const Master = (props) => {
    return(
        <>
            <Form />
        </>
    )
}

const Form = (props) => {
    const [firstName, setFirstName] = useState(null);
    const [lastName, setLastName] = useState(null);
    const [age, setAge] = useState(null);
    const [gender, setGender] = useState(null);
    const [destination, setDestination] = useState(null);
    const [nutsFree, setNutsFree] = useState(false);
    const [lactoseFree, setLactoseFree] = useState(false);
    const [vegan, setVegan] = useState(false);

    const variables = {firstName, lastName, age, gender, destination, nutsFree, lactoseFree, vegan}

    const handleSubmit = (props) => {
        console.log(3)
    }

    useEffect(()=>{
    })

    const handleChange = (e, func) => {
        func(e.target.value)
    }

    const handleChecks = (e, func) => {
        func(e.target.checked)
        console.log(e.target.checked)
    }

    const DisplayInfo = (props) => {
        return (
        <div id="results">
            <p>Your Name: {props.variables.firstName} {props.variables.lastName}</p>
            <p>Your Age: {props.variables.age}</p>
            <p>Your Gender: {props.variables.gender}</p>
            <p>Your Destination: {props.variables.destination}</p>
            <p>Your Dietary Restrictions:</p>
            <p>**Nuts Free: {props.variables.nutsFree ? "Yes" : "No"}</p>
            <p>**Lactose Free: {props.variables.lactoseFree ? "Yes" : "No"}</p>
            <p>**Vegan: {props.variables.vegan ? "Yes" : "No"}</p>

        </div>
        )}

    return (
        <>
            <div id="formDiv">
                <form id="form" onSubmit={handleSubmit}>
                    <InputWithLabel id="firstName" label="First Name" type="text" onChange={(e)=>handleChange(e, setFirstName)}/>
                    <InputWithLabel id="lastName" label="Last Name" type="text" onChange={(e)=>handleChange(e, setLastName)}/>
                    <InputWithLabel id="age" label="Age" type="text" onChange={(e)=>handleChange(e, setAge)}/>
                    <InputRadio id="mgender" label="Male" type="radio" name="gender" onChange={(e)=>handleChange(e, setGender)}/>
                    <InputRadio id="fgender" label="Female" type="radio" name="gender" onChange={(e)=>handleChange(e, setGender)}/>
                    <label htmlFor="destination">Select Your Destination</label>
                    <br/>
                    <select name="destination" id="destination" onChange={(e)=>handleChange(e, setDestination)}>
                        <option value>-- Please Choose a Destination --</option>
                        <option value="Thailand">Thailand</option>
                        <option value="Japan">Japan</option>
                        <option value="Brazil">Brazil</option>
                    </select>
                    <br/>
                    <InputWithCheck id="nutsFree" label="Nuts Free" type="checkbox" name="nutsFree" onChange={(e)=>handleChecks(e, setNutsFree)} />
                    <InputWithCheck id="lactoseFree" label="Lactose Free" type="checkbox" name="lactoseFree" onChange={(e)=>handleChecks(e, setLactoseFree)}/>
                    <InputWithCheck id="vegan" label="Vegan" type="checkbox" name="vegan" onChange={(e)=>handleChecks(e, setVegan)}/>
                    <button type="submit" value="Submit" form="form">Submit</button>
                </form>
            </div>
            <br></br>
            <DisplayInfo variables={variables}/>
        </>
    )
}

const InputWithLabel = (props) => {
    let {id, label, type, onChange} = props
    return (
        <>
            <label htmlFor={id}>{label}</label>
            <input name={id} id={id} type={type} onChange={onChange}/>
            <br/>
        </>
    )
}

const InputRadio = (props) => {
    let {id, label, type, name, onChange} = props
    return (
        <>
            <label htmlFor={id}>{label}</label>
            <input id={id} type={type} name={name} value={label} onChange={onChange}/>
            <br/>
        </>
    )
}

const InputWithCheck = (props) => {
    let {id, label, type, name, onChange} = props
    return (
        <>
            <input id={id} type={type} name={name} onChange={onChange}/>
            <label htmlFor={id}>{label}</label>
            <br/>
        </>
    )
};


export default Master