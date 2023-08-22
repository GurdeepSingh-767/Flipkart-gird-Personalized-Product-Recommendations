import React from 'react'

const Category = () => {
  return (
    <div className="w-1/4 mt-1 bg-white p-4 border border-black border-t-0 border-r-3">
      <div className="rounded-xl border-2 border-pink-600  bg-gray-100">
        <p className="  text-black  p-2   ">
          This is a demo to illustrate a recommender system that finds similar items to a given clothing article or recommend items for a customer using 4 different approaches:
        </p>
      </div>

      <form className="flex flex-col items-start">
        <div className="mb-2 mt-3">
          <input type="radio" id="category1" name="category" value="Category 1" className="mr-2" />
          <label htmlFor="category1">Find similar items</label>
        </div>
        <div className="mb-2">
          <input type="radio" id="category2" name="category" value="Category 2" className="mr-2" />
          <label htmlFor="category2">Customer Recommendations</label>
        </div>
        <div className="mb-2">
          <input type="radio" id="category3" name="category" value="Category 3" className="mr-2" />
          <label htmlFor="category2">Product Captioning</label>
        </div>
        <div className="mb-2">
          <input type="radio" id="category4" name="category" value="Category 4" className="mr-2" />
          <label htmlFor="category2">Documentation</label>
        </div>

        {/* Submit button */}
        <button type="submit" className="nline-flex text-black  border-2 border-pink-600 py-2 px-6 focus:outline-pink-600 hover:bg-pink-600 hover:text-white rounded text-lg">
          Get Result
        </button>

      </form>


    </div>
  )
}

export default Category