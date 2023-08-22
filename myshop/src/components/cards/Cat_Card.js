import React, { useState, useEffect } from 'react';

const Cat_Card = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch products from the API
    fetch('http://127.0.0.1:8000/api/recommend/') // Replace with the actual API endpoint
      .then(response => response.json())
      .then(data => {
        setProducts(data); // Assuming the API response is an array of products
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div className="container px-5 py-3 mx-8 mx-auto border border-3 border-opacity-70">
      <div className="border-1 flex flex-wrap">
        {products.map(product => (
          <div key={product.product_id} className="lg:w-1/4 md:w-1/2 p-4 w-full border border-opacity-70">
            <a className="block h-48 rounded overflow-hidden">
              <img alt="product" className="object-cover object-center w-full h-full block" src={product.img_link} />
            </a>
            <div className="mt-4">
              <h3 className="text-gray-500 text-xs tracking-widest title-font mb-1">{product.category}</h3>
              <h2 className="text-gray-900 title-font text-lg font-medium">{product.product_name}</h2>
              <p className="mt-1">${product.discounted_price}</p>
              <p className="text-gray-500">${product.actual_price}</p>
              <p className="text-gray-500">Rating: {product.rating}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Cat_Card;
