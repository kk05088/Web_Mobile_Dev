import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

// import your components here
import Home from './Components/home';
import Admin from './Components/admin';

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/home">Home</Link>
          </li>
          <li>
            <Link to="/Admin">Admin</Link>
          </li>
          
        </ul>
      </nav>

      <Routes>
        <Route path="/" />
        <Route path="/admin" element={<Admin />} />
        <Route path="/home" element={<Home />} />
        
      </Routes>
    </Router>
  );
}

export default App;
