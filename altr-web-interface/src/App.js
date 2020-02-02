import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import Navbar from './components/navbar/Navbar'
import Map from './components/map/Map'
import Admin from './components/admin/Admin'
import './App.css'

function App() {
  return (
    <div className="App" onScroll="no">
      <BrowserRouter>
          <div>
              {/* <Navbar /> */}
              <Route exact path='/' component={Map}/>
              <Route exact path='/admin' component={Admin}/>
          </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
