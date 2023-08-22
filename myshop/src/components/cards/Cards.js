import React, { useState, useEffect } from 'react';

const Cards = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch products from your API here
    fetch('http://127.0.0.1:8000/api/recommend/')
      .then(response => response.json())
      .then(data => setProducts(data.recommended_products))
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  // Function to group products by category
  const groupProductsByCategory = () => {
    const groupedProducts = {};
    products.forEach(product => {
      if (!groupedProducts[product.category]) {
        groupedProducts[product.category] = [];
      }
      groupedProducts[product.category].push(product);
    });
    return groupedProducts;
  };

  const groupedProducts = groupProductsByCategory();

  return (
    <div className="container px-5 py-3 mx-8 mx-auto ">
      {Object.keys(groupedProducts).map(category => (
        <div key={category} className="mb-6">
          <h1 className="text-black text-2xl font-bold flex items-start px-5 py-4 ">{category}</h1>
          <div className="flex flex-wrap m-4">
            {groupedProducts[category].slice(0, 4).map(product => (
             
               <div class="lg:w-1/4  p-4 w-full border border-opacity-70   ">
               <a class="block h-48 rounded overflow-hidden">
                 <img alt="ecommerce" class="object-cover object-center w-full h-full block" src={product.img_link}/>
               </a>
               <div class="mt-4">
                 <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">{product.category}</h3>
                 <h2 class="text-gray-900 title-font text-lg font-medium">{product.product_name}</h2>
                 <p class="mt-1">₹{product.discounted_price}</p>
               </div>
           </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};

export default Cards;
