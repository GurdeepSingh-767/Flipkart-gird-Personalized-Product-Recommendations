import React from 'react';
import Header from '../components/header/index'
import Hero from '../components/hero/index';
import Cards from '../components/cards/Cards';
import Cat_Card from '../components/cards/Cat_Card';
import Testimonials from '../components/testimonals/Testimonals';
import Footer from '../components/footer/Footer';
const Home = () => {
  return (
    <div>
      <Header/>
      <Hero/>
      <div className="flex flex-col text-center w-full ">
        <h2 className="text-xs text-pink-600 font-medium mb-1">PRODUCTS</h2>
        <div className="sm:text-3xl text-2xl font-medium text-black">MOST POPULAR PRODUCTS</div>
      </div>
      <Cards />
      <Testimonials />
      <Footer />
    </div>
  )
}

export default Home
