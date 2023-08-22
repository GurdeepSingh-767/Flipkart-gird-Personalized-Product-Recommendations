from django.db import models
# from db_conn import db


# Create your models here.
class User(models.Model):
    user_name= models.CharField(max_length=50,unique=True)
    password= models.CharField(max_length=50)
    def __str__(self):
        return self.user_name
    
        
class Product(models.Model):
    product_id= models.CharField(max_length=50,unique=True)
    product_name= models.CharField(max_length=200)
    category= models.CharField(max_length=200)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    rating_count = models.IntegerField()
    about_product = models.CharField(max_length=200)
    review_id = models.CharField(max_length=50)
    review_title = models.CharField(max_length=200)
    review_content = models.CharField(max_length=300)
    img_link = models.URLField()
    def __str__(self):
        return self.product_name
# user_collection= db['user']