import './App.css';
import React from "react";
import {useState} from "react";


class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {message: null}

  }
  async componentDidMount() {
    const url = "http://localhost:3000/api/hello";
    try {
      const response = await fetch(url);
      const data = await response.json();
      this.message = data.msg
      this.setState({message: data.msg})
    } catch (error) {
      console.log(error)
    }
  }
  render(){
    return <h1>{this.state.message}</h1>
  }
};



const Form = (props) => {
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault()
    const userInput = document.querySelector("#blah").value;
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({userInput})
    }
    const response = await fetch("http://localhost:3000/api/world", options)
    const data = await response.json();
    setMessage(data.message)
  }

  return (
    <>
      <form method="POST" onSubmit={handleSubmit}>
        <label htmlFor="blah">Enter your stuff:</label>
        <input type="text" id="blah"></input>
        <button type="submit">Submit</button>
      </form>
      <p id="messageBos">{message}</p>
    </>
  )
}
export default Form