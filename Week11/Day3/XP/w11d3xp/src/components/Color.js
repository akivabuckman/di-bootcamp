import React from 'react';
import { useState, useEffect } from "react";

// const Color = () => {
//     const [favoriteColor, setFavoriteColor] = useState("red")

//     const changeColor = () => {
//         setFavoriteColor("blue")
//     }

//     useEffect(()=>{
//         alert(`useEffect reached - color changed to ${favoriteColor}`)
//     }, [favoriteColor])
    
//     return(
//         <>
//         <h1>My Favorite Color is {favoriteColor}</h1>
//         <button onClick={changeColor}>Change Color</button>
//         </>
//     )
// };

class Color extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            favoriteColor: "red",
            show: true
        }
    }

    changeColor = () => {
        this.setState({favoriteColor: "blue"})
    }

    shouldComponentUpdate = () => true

    componentDidUpdate(prevProps, prevState) {
        alert(`new color is ${this.state.favoriteColor}`)
        console.log("after update")
    }

    changetoYellow = () => {this.setState({favoriteColor: "yellow"})};

    componentDidMount() {setTimeout(this.changetoYellow, 2000)};

    getSnapshotBeforeUpdate = () => {
        console.log("in getSnapshotBeforeUpdate")
        return true;
    }

    render(){
        return(
            <>
            <h1>My Favorite Color is {this.state.favoriteColor}</h1>
            <button onClick={this.changeColor}>Change Color</button>
            </>
        )
    }


}

class Child extends React.Component {
    componentWillUnmount = () => {alert("unmounted")}

    render(){
        return <h1>Hello World!</h1>
    }
}

class App1 extends React.Component {
    constructor(props){
        super(props);
        this.state = {show: true}
    }

    deleteHeader = () => {this.setState({show: false})}

    render(){
        if (this.state.show) {
            this.child = <Child /> 
        } else {
            this.child = null
        }
        return (
            <>
                {this.child}
                <button onClick={this.deleteHeader}>Delete Header</button>
            </>
        )
    }
}
export default App1