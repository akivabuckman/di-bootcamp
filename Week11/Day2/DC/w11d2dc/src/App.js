// import { useState, useEffect } from "react";
import React from "react";

import LanguageMaker from "./components/LanguageMaker.js"
export default class App extends React.Component {
  constructor(){
    super();
    this.state = {
      languages: [
        {name: "Php", votes: 0},
        {name: "Python", votes: 0},
        {name: "JavaSript", votes: 0},
        {name: "Java", votes: 0}
      ]
    };
  };
    
  handleClick = (language) => {
    for (let i of this.state.languages) {
      if (i.name === language.name) {
        i.votes ++
      }
    };
    this.setState({languages: this.state.languages})
  }
  
  // render() {
  //   return (
  //     <>
  //       <h1>Vote for your favorite language</h1>
  //       {this.state.languages.map(language => (
  //         <React.Fragment key={language.name}>
  //           <LanguageMaker language={language} />
  //           <button onClick={() => this.handleClick(language)}>Click Here</button>
            
  //         </React.Fragment>
  //       ))}
  //     </>
  //   );
  // }
  render() {
    return (
      <>
        <h1>Vote for your favorite language</h1>
        {this.state.languages.map(language => (
          <React.Fragment key={language.name}>
            <LanguageMaker language={language} handleClick={this.handleClick}/>
          </React.Fragment>
        ))}
      </>
    );
  }
}