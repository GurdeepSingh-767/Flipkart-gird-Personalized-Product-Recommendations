from django.urls import path
from . import views
from .views import get_recommendations
urlpatterns= [
    path('users/',views.UserList.as_view()),
    path('update/<int:pk>/', views.UserDetail.as_view()),
    path('add/', views.UserCreate.as_view()),
    path('register/', views.register_user, name='register'),
    path('login/', views.user_login, name='login'),
    path('register_product/', views.register_product, name='register_p'),
    path('products/',views.ProductList.as_view()),
    path('recommend/', get_recommendations, name='get_recommendations'),
    path('user/<str:username>/', views.get_recommendations_user, name='get_user_data'),
    path('predicted/<str:username>/', views.get_predicted_recommendations, name='get_predicted_data'),
    # path('show/',views.get_all_person),
]