import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from "./screens/Header";
import Main from "./screens/Main";
import Clean from './screens/Clean';
import Clean_more from './screens/Clean_more';
import Funding from './screens/Funding';
import Footer from "./screens/Footer";
import Fd_Detail from "./screens/Fd_Detail";
import Farmer from "./screens/Farmer";
import Farm from "./screens/Farm";
import Ask from "./screens/Ask";
import React, { useEffect, useState } from 'react';
import Mmenu from './screens/Mmenu';
function App() {
  return (
    <React.StrictMode>
      <div id='wrap'>
        <BrowserRouter>
          <Header />
          <Routes>
            <Route path="/" element={<Main />}></Route>
            <Route path="/Clean" element={<Clean />}></Route>
            <Route path="/Clean_more" element={<Clean_more />}></Route>
            <Route path="/Ask" element={<Ask />}></Route>
            <Route path="/Funding" element={<Funding />}></Route>
            <Route path="/Fd_Detail" element={<Fd_Detail />}></Route>
            <Route path="/Farmer" element={<Farmer />}></Route>
            <Route path="/Farm" element={<Farm />}></Route>
          </Routes>
          <Footer />
          <Mmenu />
        </BrowserRouter>
      </div>
    </React.StrictMode>
  );
}

export default App;
