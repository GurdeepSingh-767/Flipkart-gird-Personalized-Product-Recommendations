import numpy as np
import pandas as pd


df = pd.read_csv('product_detail.csv')

# Calculate the average rating for each product 
average_rating = df.groupby('product_id')['rating'].mean()

#Calculate the count of ratings for each product
count_rating = df.groupby('product_id')['rating_count'].mean()

#Create a dataframe with calculated average and count of ratings
final_rating = pd.DataFrame({'avg_rating':average_rating, 'rating_count':count_rating})

#Sort the dataframe by average of ratings
final_rating = final_rating.sort_values(by='avg_rating',ascending=False)

final_rating.head()


def top_n_products(final_rating, n, min_interaction):
    
    #Finding products with minimum number of interactions
    recommendations = final_rating[final_rating['rating_count']>min_interaction]
    
    #Sorting values w.r.t average rating 
    recommendations = recommendations.sort_values('avg_rating',ascending=False)
    
    return recommendations.index[:n]


top_products=list(top_n_products(final_rating, 5, 50))
print(top_products)