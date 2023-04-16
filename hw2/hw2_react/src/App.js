import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

// import your components here
import Home from './Components/home';
import Admin from './Components/admin';
import Login from './Components/login';
function App() {
  return (
    <Router>

      {/* <nav>
        <ul>
          <li>
            <Link to="/home">Home</Link>
          </li>
          <li>
            <Link to="/Admin">Admin</Link>
          </li>
          
        </ul>
      </nav> */}

      <Routes>
        <Route path="/" element={<Login/>}/>
        <Route exact path="/Admin"  element={<Admin/>} />
        <Route exact path="/home"  element={<Home/>} />
        
      </Routes>
    </Router>
  );
}

export default App;
