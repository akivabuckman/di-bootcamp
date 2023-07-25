import './App.css';
import React from "react";
import BuggyCounter from './components/BuggyCounter';
import ErrorBoundary from './components/ErrorBoundary';



function App() {
  return (
    <div className="App">
      <ErrorBoundary>
        <BuggyCounter />
      </ErrorBoundary>
      <ErrorBoundary>
        <BuggyCounter />
      </ErrorBoundary>
    </div>
  );
}

export default App;
