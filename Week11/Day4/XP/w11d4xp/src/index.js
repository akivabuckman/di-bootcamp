import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import XP4 from './App';
import reportWebVitals from './reportWebVitals';
import Example1 from './components/Example1';
import Example2 from './components/Example2';
import Example3 from './components/Example3';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <XP4 />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
