import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import Home from './Home';
import Login from './Login';
import { AuthProvider } from './Auth';
import PrivateRoute from './PrivateRoute';

function Admin() {
  return (
    <AuthProvider>
      <BrowserRouter>
          <div>
              <PrivateRoute exact path='/admin' component={Home}/>
              <Route exact path='/login' component={Login}/>
          </div>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default Admin;
