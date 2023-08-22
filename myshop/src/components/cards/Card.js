import React from 'react'

const Card = () => {
  return (
    <div className="container px-5 py-20 mx-auto">
      <div class="lg:w-1/4 md:w-1/2 p-4 w-full border border-opacity-70 ">
        <a class="block h-48 rounded overflow-hidden">
          <img alt="ecommerce" class="object-cover object-center w-full h-full block" src="https://dummyimage.com/420x260"/>
        </a>
        <div class="mt-4">
          <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">CATEGORY</h3>
          <h2 class="text-gray-900 title-font text-lg font-medium">The Catalyzer</h2>
          <p class="mt-1">$16.00</p>
        </div>
    </div>
    </div>
  )
}

export default Card