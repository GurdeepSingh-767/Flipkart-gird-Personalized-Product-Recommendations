from django.shortcuts import get_object_or_404, render
from .models import User,Product
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView, ListCreateAPIView

import numpy as np
import pandas as pd
from django.templatetags.static import static
from sklearn.metrics.pairwise import cosine_similarity


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer,ProductSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def index(request):
    return HttpResponse("<h1>App is running...</h1>")



# def add_user(request):
#     records={
#         "user_name": "Mustkeem",
#         "password": "12345"
#     }
#     user_collection.insert_one(records)
#     return HttpResponse("New user added")

# def get_all_person(request):
#     persons = user_collection.find()
#     return HttpResponse(persons)

class UserList(ListAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer

class UserCreate(ListCreateAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset= User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        user_name = request.data.get("user_name")
        password = request.data.get("password")

        print(user_name, password)
        
        try:
            user = User.objects.get(user_name=user_name)
        except ObjectDoesNotExist:
            user = None
        if not user:
            return Response({'User not found'})
        if user and user.password==password:
            # Authentication successful, generate a token or perform other actions
            return Response({'Accessed':'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({   }, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
def register_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductList(ListAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer











# # Calculate the average rating for each product 



# def top_n_products(final_rating, n, min_interaction):
    
#     #Finding products with minimum number of interactions
#     recommendations = final_rating[final_rating['rating_count']>min_interaction]
    
#     #Sorting values w.r.t average rating 
#     recommendations = recommendations.sort_values('avg_rating',ascending=False)
    
#     return list(recommendations.index[:n])

# @api_view(['GET'])
# def get_recommendations(request):
#     n = 8  # Number of recommended products
#     min_interaction = 50  # Minimum interaction threshold

#     df = pd.read_csv('product_detail.csv')

#     average_rating = df.groupby('product_id')['rating'].mean()

#     #Calculate the count of ratings for each product
#     count_rating = df.groupby('product_id')['rating_count'].mean()

#     #Create a dataframe with calculated average and count of ratings
#     final_rating = pd.DataFrame({'avg_rating':average_rating, 'rating_count':count_rating})

#     #Sort the dataframe by average of ratings
#     final_rating = final_rating.sort_values(by='avg_rating',ascending=False)

#     # Implement your logic to calculate recommended products
#     recommended_product_ids = top_n_products(final_rating, n, min_interaction)
#     print(recommended_product_ids)

#     recommended_products = Product.objects.filter(product_id__in=recommended_product_ids)
#     print(recommended_product_ids)

#     serialized_products = []
#     for product in recommended_products:
#         serialized_products.append({
#             'product_id': product.product_id,
#             'product_name': product.product_name,
#             'category': product.category,
#             'discounted_price': product.discounted_price,
#             'actual_price': product.actual_price,
#             'discounted_percentage': product.discount_percentage,
#             'rating': product.rating,
#             'rating_count': product.rating_count,
#             'about_product': product.about_product,
#             'review_id': product.review_id,
#             'review_content': product.review_content,
#             'img_link': product.img_link
#         })

#     return Response({'recommended_products': serialized_products})



def top_n_products(final_rating, n):
    # Sorting values w.r.t rating_count in descending order and selecting the top n
    top_products = final_rating.nlargest(n, 'rating_count')
    
    # Sorting values w.r.t average rating 
    recommendations = top_products.sort_values('avg_rating', ascending=False)
    
    return list(recommendations['product_id'])

@api_view(['GET'])
def get_recommendations(request):
    n = 4  # Number of recommended products

    # Read data from CSV file
    df = pd.read_csv('product_detail.csv')

    category_product_count = df['category'].value_counts()

    # Filter categories with more than min_products_per_category products
    valid_categories = category_product_count[category_product_count >= n].index

    # Filter data to include only valid categories
    df_valid_categories = df[df['category'].isin(valid_categories)]

    # Group the data by category
    category_groups = df_valid_categories.groupby('category')

    # Initialize a list to store all recommended products
    all_recommended_products = []
    

    # Iterate through each category group
    for category, group_data in category_groups:
        # Sort the group data by average rating
        category_final_rating = group_data.groupby('product_id')['rating'].mean().reset_index()
        category_final_rating = category_final_rating.rename(columns={'rating': 'avg_rating'})

        # Calculate the count of ratings for each product in the category
        category_count_rating = group_data.groupby('product_id')['rating_count'].mean().reset_index()
        category_final_rating = pd.merge(category_final_rating, category_count_rating, on='product_id')

        # Sort the category final rating data
        category_final_rating = category_final_rating.sort_values(by='avg_rating', ascending=False)

        # Implement your logic to calculate recommended products for this category
        recommended_product_ids = top_n_products(category_final_rating, n)
        print(recommended_product_ids)

        all_recommended_products.extend(recommended_product_ids)

    # Retrieve recommended products from Django model
    recommended_products = Product.objects.filter(product_id__in=all_recommended_products)

    serialized_products = []
    for product in recommended_products:
        serialized_products.append({
            'product_id': product.product_id,
            'product_name': product.product_name,
            'category': product.category,
            'discounted_price': product.discounted_price,
            'actual_price': product.actual_price,
            'discounted_percentage': product.discount_percentage,
            'rating': product.rating,
            'rating_count': product.rating_count,
            'about_product': product.about_product,
            'review_id': product.review_id,
            'review_content': product.review_content,
            'img_link': product.img_link
        })
    # Define a custom sorting key function
    def sorting_key(item):
        return item['category']

    # Sort the data list based on the sorting key
    serialized_products = sorted(serialized_products, key=sorting_key)
    return Response({'recommended_products': serialized_products})



# defining a function to get similar users
def similar_users(user_index, interactions_matrix):
    similarity = []
    for user in range(0, interactions_matrix.shape[0]): #  .shape[0] gives number of rows
        
        #finding cosine similarity between the user_id and each user
        sim = cosine_similarity([interactions_matrix.loc[user_index]], [interactions_matrix.loc[user]])
        
        #Appending the user and the corresponding similarity score with user_id as a tuple
        similarity.append((user,sim))
        
    similarity.sort(key=lambda x: x[1], reverse=True)
    most_similar_users = [tup[0] for tup in similarity] #Extract the user from each tuple in the sorted list
    similarity_score = [tup[1] for tup in similarity] ##Extracting the similarity score from each tuple in the sorted list
   
    #Remove the original user and its similarity score and keep only other similar users 
    most_similar_users.remove(user_index)
    similarity_score.remove(similarity_score[0])
       
    return most_similar_users, similarity_score

# defining the recommendations function to get recommendations by using the similar users' preferences
def recommendations(user_index, num_of_products, interactions_matrix):
    
    #Saving similar users using the function similar_users defined above
    most_similar_users = similar_users(user_index, interactions_matrix)[0]
    
    #Finding product IDs with which the user_id has interacted
    prod_ids = set(list(interactions_matrix.columns[np.where(interactions_matrix.loc[user_index] > 0)]))
    recommendations = []
    
    observed_interactions = prod_ids.copy()
    for similar_user in most_similar_users:
        if len(recommendations) < num_of_products:
            
            #Finding 'n' products which have been rated by similar users but not by the user_id
            similar_user_prod_ids = set(list(interactions_matrix.columns[np.where(interactions_matrix.loc[similar_user] > 0)]))
            recommendations.extend(list(similar_user_prod_ids.difference(observed_interactions)))
            observed_interactions = observed_interactions.union(similar_user_prod_ids)
        else:
            break
    
    return recommendations[:num_of_products]

def get_integer_index(matrix,user_index_str):
        try:
            user_index = matrix.index.get_loc(user_index_str)
            return user_index
        except KeyError:
            # Handle the case when user_index_str is not in the index
            return None


@api_view(['GET'])
def get_recommendations_user(request,username):
    df_user = pd.read_csv('preprocessed_user.csv')

    df_grouped = df_user.groupby(['user_id', 'product_id'])['rating'].mean().reset_index()

    #Creating the interaction matrix of products and users based on ratings and replacing NaN value with 0
    final_ratings_matrix = df_grouped.pivot(index = 'user_id', columns ='product_id', values = 'rating').fillna(0)
    final_ratings_matrix1 = df_grouped.pivot(index = 'user_id', columns ='product_id', values = 'rating').fillna(0)


    final_ratings_matrix['user_index'] = np.arange(0, final_ratings_matrix.shape[0])
    final_ratings_matrix.set_index(['user_index'], inplace=True)

    
    user_id = df_user.loc[(df_user['user_name'] == username), 'user_id'].values[0]
    print(user_id,'k')
    user_index=get_integer_index(final_ratings_matrix1,user_id)
    product_ids=recommendations(user_index,4,final_ratings_matrix)
    print(product_ids)

     # Retrieve recommended products from Django model
    recommended_products = Product.objects.filter(product_id__in=product_ids)



    serialized_products = []
    for product in recommended_products:
        serialized_products.append({
            'product_id': product.product_id,
            'product_name': product.product_name,
            'category': product.category,
            'discounted_price': product.discounted_price,
            'actual_price': product.actual_price,
            'discounted_percentage': product.discount_percentage,
            'rating': product.rating,
            'rating_count': product.rating_count,
            'about_product': product.about_product,
            'review_id': product.review_id,
            'review_content': product.review_content,
            'img_link': product.img_link
        })

    return Response({'recommended_products': serialized_products})

from scipy.sparse import csr_matrix, find
import numpy as np
from scipy.sparse.linalg import svds

import numpy as np

import numpy as np

def recommend_items(user_index, interactions_matrix, preds_matrix,final_ratings_matrix, num_recommendations):
    
    # Get the user's ratings from the actual and predicted interaction matrices
    user_ratings = interactions_matrix[user_index,:].toarray().reshape(-1)
    user_predictions = preds_matrix[user_index,:].toarray().reshape(-1)

    #Creating a dataframe with actual and predicted ratings columns
    temp = pd.DataFrame({'user_ratings': user_ratings, 'user_predictions': user_predictions})
    temp['Recommended Products'] = np.arange(len(user_ratings))
    temp = temp.set_index('Recommended Products')
    
    #Filtering the dataframe where actual ratings are 0 which implies that the user has not interacted with that product
    temp = temp.loc[temp.user_ratings == 0]   
    
    # Recommending products with top predicted ratings
    temp = temp.sort_values('user_predictions', ascending=False)  # Sort the dataframe by user_predictions in descending order
    
    # Extract the indices of the recommended products
    recommended_indices = temp.index[:num_recommendations]
    
    # Map indices to product IDs using final_ratings_matrix.columns
    recommended_product_ids = final_ratings_matrix.columns[recommended_indices]
    
    return recommended_product_ids
    



@api_view(['GET'])
def get_predicted_recommendations(request,username):

    df_user = pd.read_csv('preprocessed_user.csv')

    df_grouped = df_user.groupby(['user_id', 'product_id'])['rating'].mean().reset_index()

    #Creating the interaction matrix of products and users based on ratings and replacing NaN value with 0
    final_ratings_matrix = df_grouped.pivot(index = 'user_id', columns ='product_id', values = 'rating').fillna(0)
    final_ratings_matrix1 = df_grouped.pivot(index = 'user_id', columns ='product_id', values = 'rating').fillna(0)


    final_ratings_matrix['user_index'] = np.arange(0, final_ratings_matrix.shape[0])
    final_ratings_matrix.set_index(['user_index'], inplace=True)

    # Create a sparse matrix
    final_ratings_sparse = csr_matrix(final_ratings_matrix.values)
    
    # Singular Value Decomposition
    U, s, Vt = svds(final_ratings_sparse, k = 1000) # here k is the number of latent features

    # Construct diagonal array in SVD
    sigma = np.diag(s)

    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) 

    # Predicted ratings
    preds_df = pd.DataFrame(abs(all_user_predicted_ratings), columns = final_ratings_matrix.columns)
    print(preds_df)
    preds_matrix = csr_matrix(preds_df.values)

    user_id = df_user.loc[(df_user['user_name'] == username), 'user_id'].values[0]
    print(user_id,'k')
    user_index=get_integer_index(final_ratings_matrix1,user_id)
    print(user_index)
    #Enter 'user index' and 'num_recommendations' for the user
    product_ids=recommend_items(user_index,final_ratings_sparse,preds_matrix,final_ratings_matrix,4)
    
     # Retrieve recommended products from Django model
    recommended_products = Product.objects.filter(product_id__in=product_ids)
    



    serialized_products = []
    for product in recommended_products:
        serialized_products.append({
            'product_id': product.product_id,
            'product_name': product.product_name,
            'category': product.category,
            'discounted_price': product.discounted_price,
            'actual_price': product.actual_price,
            'discounted_percentage': product.discount_percentage,
            'rating': product.rating,
            'rating_count': product.rating_count,
            'about_product': product.about_product,
            'review_id': product.review_id,
            'review_content': product.review_content,
            'img_link': product.img_link
        })
    
    print(serialized_products)

    return Response({'recommended_products': serialized_products})
    

