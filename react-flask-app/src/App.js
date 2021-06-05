import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const [currentTime, setCurrentTime] = useState(0);

  const [ola, setOla] = useState();

  useEffect(() => {
    fetch('/time').then(response => response.json()).then(data => {
      setCurrentTime(data.time);
    })
  }, []);

  useEffect(() => {
    fetch('/ola').then(resp => resp.json()).then(data => {
      setOla(data.ola);
    })
  })

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>The current time is {currentTime}.</p>
        <p>{ola}</p>
      </header>
    </div>
  );
}

export default App;
