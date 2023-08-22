import React from 'react';
import Cards from '../cards/Cards';
import RCard from '../cards/Rcard';
import PCard from '../cards/Pcard';

const Recommended = () => {
  return (

    <div className="w-3/4 ml-5">
      <PCard />
      <RCard />
      <Cards />
    </div>

  )
}

export default Recommended