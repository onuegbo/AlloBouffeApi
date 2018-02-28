from rest_framework import serializers
from allobouffe.models import Restaurant, Product
from django.contrib.auth.models import User



class RestaurantSerializer(serializers.ModelSerializer):
      created  = serializers.ReadOnlyField(source='created.username')
      products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
     
      class Meta:
        model = Restaurant
        fields = ('id', 'name', 'addresse', 'description', 'telephone', 'is_hidden', 'created', 'products')


class ProductSerializer(serializers.ModelSerializer):
    
    
      class Meta:
        model = Product
        fields = ('id', 'name', 'delivery_time', 'description', 'price')
        


class UserSerializer(serializers.ModelSerializer):

     restaurant = serializers.PrimaryKeyRelatedField(many=True, queryset=Restaurant.objects.all())
     
     class Meta:
        model = User
        fields = ('id', 'username', 'restaurant')