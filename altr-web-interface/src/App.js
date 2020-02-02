import React from 'react';
import Navbar from './components/navbar/Navbar'
import Map from './components/map/Map'
import './App.css'

function App() {
  return (
    <div className="App" onScroll="no">
      <Navbar />
      <Map />
    </div>
  );
}

export default App;
