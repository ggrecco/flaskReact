import React, { useEffect, useState } from 'react';
import './App.css';

function App() {

  const [ola, setOla] = useState();

  useEffect(() => {
    fetch('ola').then(res => res.json()).then(data => {
      setOla(data.ola);
    });
  });

  return (
    <div className="App">
    <header className="App-header">
      <p>{ola}</p>
    </header>
  </div>
  );
}

export default App;
