import React from 'react';

const style_header = {
    color: "white",
    backgroundColor: "DodgerBlue",
    padding: "10px",
    fontFamily: "Arial"
  };

class Exercise extends React.Component {
    render() {
        return <>
        <h1 style={style_header}>This is a header</h1>
        <p class="para">This is a paragraph</p>
        <a href="#">This is a link</a>
        <form>
            <h4>This is a form</h4>
            <label for="name">Enter your name:</label>
            <input id="name" type="text"></input>
            <input type="submit" value="submit"></input>
            <h5>Here's an image:</h5>
            <img src="https://www.w3schools.com/images/w3schools_green.jpg"></img>
            <h5>Here's a list:</h5>
            <ul>
                <li>Coffee</li>
                <li>Tea</li>
                <li>Milk</li>
            </ul>
        </form>
        </>;
    }
}

export default Exercise;