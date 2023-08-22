import React from 'react';
import Header from '../components/header/index';
import Category from '../components/sidebar/Category'
import Recommended from '../components/recommended/Recommended';
// import Card from '../components/cards/Card';
import Footer from '../components/footer/Footer';

const Main = () => {
  return (
    <div>
      <Header />
      <div className="flex  ">
        <Category />
        <Recommended/>
        </div>
        <Footer />
    </div>
  )
}

export default Main