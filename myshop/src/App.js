// App.js
import React from 'react';
import { useState, useEffect } from 'react';
import axios from "axios";
import './App.css';
// import axios from 'axios';
import Home from './pages/Home';

function App() {
  return (
    <div className="App">
      <Home />
    </div>
  );
}

export default App;
