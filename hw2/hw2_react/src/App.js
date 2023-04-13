import logo from './logo.svg';
import './App.css';
import Header from './header';
import Footer from './footer';
import Home from './home';
import Projects from './projects';
import React from "react";
import ReactDOM from 'react-dom';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  useRoutes,
  BrowserRouter
} from "react-router-dom";




function App() {
  return (
    <BrowserRouter>
    <div className="App">
      <Routes>
        <Route path="/" element={ <Home/> } />
        {/* <Route path="about" element={ <About/> } /> */}
        <Route path="Projets" element={ <Projects/> } />
      </Routes>
    </div>
    </BrowserRouter>

    
  );
}

export default App;
