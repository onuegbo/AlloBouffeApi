from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from allobouffe.serializer import RestaurantSerializer, ProductSerializer
from allobouffe.serializer import UserSerializer
from allobouffe.permissions import IsOwnerOrReadOnly


from allobouffe.models import Restaurant, Product
from django.contrib.auth.models import User




#REST framework includes a number of permission classes that we can use to restrict who can access a given view


class RestaurantViewSet(viewsets.ModelViewSet):

    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
  
    """

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)  

    #associate restaurant with the user that created them
    def perform_create(self, serializer):
        serializer.save(created =self.request.user)


class ProductViewSet(viewsets.ModelViewSet):

    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)  



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

