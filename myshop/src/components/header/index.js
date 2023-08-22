import React, { useState } from 'react'
import MyModal from './MyModal'

const Header = () => {
  const username = sessionStorage.getItem('user_name');
  
  const[showMyModal, setShowMyModal] = useState(false);

  const handleOnClose =() => setShowMyModal(false);
  return (
    <div>
      <header className="text-black-600 body-font shadow-lg">
  <div className="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
    <a className="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" className="w-10 h-10 text-white p-2 bg-pink-600 rounded-full" viewBox="0 0 24 24">
        <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"></path>
      </svg>
      <span className="ml-3 text-xl">MYSHOP</span>
    </a>
    <nav className="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
      <a className="mr-5 hover:text-gray-900">HOME</a>
      <a className="mr-5 hover:text-gray-900">PRODUCTS</a>
      <a className="mr-5 hover:text-gray-900">ABOUT US</a>
      <a className="mr-5 hover:text-gray-900">CONTACT</a>
    </nav>
    <button onClick={() =>setShowMyModal(true)} className="inline-flex items-center bg-gray-100 border-0 py-3 px-3 focus:outline-none hover:bg-pink-600 hover:text-white rounded text-base mt-4 md:mt-0">Login
      <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" className="w-4 h-4 ml-1" viewBox="0 0 24 24">
        <path d="M5 12h14M12 5l7 7-7 7"></path>
      </svg>
    </button>
    <MyModal onClose={handleOnClose} visible={showMyModal}/>
  </div>
 
</header>
    </div>
  )
}

export default Header
