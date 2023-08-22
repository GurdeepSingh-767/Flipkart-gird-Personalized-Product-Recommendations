from rest_framework import serializers
from .models import User, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['user_name', 'password']

    def create(self, validated_data):
        user = User(
            user_name=validated_data['user_name'],
            password=validated_data['password']
        )
        user.save()
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= ['product_id', 'product_name', 'category', 'discounted_price',
       'actual_price', 'discount_percentage', 'rating', 'rating_count',
       'about_product', 'review_id', 'review_title', 'review_content',
       'img_link']

    def create(self, validated_data):
        product = Product(
            product_id=validated_data['product_id'],
            product_name=validated_data['product_name'],
            category=validated_data['category'],
            discounted_price=validated_data['discounted_price'],
            actual_price=validated_data['actual_price'],
            discount_percentage=validated_data['discount_percentage'],
            rating=validated_data['rating'],
            rating_count=validated_data['rating_count'],
            about_product=validated_data['about_product'],
            review_id=validated_data['review_id'],
            review_title=validated_data['review_title'],
            review_content=validated_data['review_content'],
            img_link=validated_data['img_link']
        )
        product.save()
        return product