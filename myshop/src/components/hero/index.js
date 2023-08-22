import React from 'react';

import laptop from '../../assets/images/latop.jpg'

function Hero() {
  return (
    <div>
          <section className="text-gray-600 body-font px-8">
  <div className="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
    <div className="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
      <h1 className="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Before they sold out
        
      </h1>
      <p className="mb-8 leading-relaxed">Copper mug try-hard pitchfork pour-over freegan heirloom neutra air plant cold-pressed tacos poke beard tote bag. Heirloom echo park mlkshk tote bag selvage hot chicken authentic tumeric truffaut hexagon try-hard chambray.</p>
      <div className="flex justify-center">
        <button className="inline-flex text-black  border-2 border-pink-600 py-2 px-6 focus:outline-pink-600 hover:bg-pink-600 hover:text-white rounded text-lg">SHOP NOW</button>
        <button className="ml-4 inline-flex text-white bg-pink-600 border-0 py-2 px-6 focus:outline-none  rounded text-lg">ADD TO CARD</button>
      </div>
    </div>
    <div className="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
    <img
      classNameName="object-cover object-center rounded"
      alt="hero"
      src={laptop}
    />
    </div>
  </div>
</section>
    </div>
  )
}

export default Hero