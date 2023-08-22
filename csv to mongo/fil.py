import numpy as np
import pandas as pd


def get_integer_index(matrix,user_index_str):
        try:
            user_index = matrix.index.get_loc(user_index_str)
            return user_index
        except KeyError:
            # Handle the case when user_index_str is not in the index
            return None


df_user = pd.read_csv('preprocessed_user.csv')

df_grouped = df_user.groupby(['user_id', 'product_id'])['rating'].mean().reset_index()

    #Creating the interaction matrix of products and users based on ratings and replacing NaN value with 0
final_ratings_matrix = df_grouped.pivot(index = 'user_id', columns ='product_id', values = 'rating').fillna(0)
final_ratings_matrix1 = df_grouped.pivot(index = 'user_id', columns ='product_id', values = 'rating').fillna(0)


final_ratings_matrix['user_index'] = np.arange(0, final_ratings_matrix.shape[0])
final_ratings_matrix.set_index(['user_index'], inplace=True)

    
user_id = df_user.loc[(df_user['user_name'] == 'Mithila Saha'), 'user_id'].values[0]
print(user_id,'k')
user_index=get_integer_index(final_ratings_matrix1,user_id)
print(user_index)

# df['rating'] = df['rating'].str.replace(',', '').astype(float)

# df.to_csv("user.csv", index=False)