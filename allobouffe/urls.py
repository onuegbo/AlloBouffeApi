from django.urls import path
from django.conf.urls import include, url

# from django.conf.urls.static import static
# from django.conf import settings
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'restaurant', views.RestaurantViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'users', views.UserViewSet)


app_name = 'allobouffe'
urlpatterns = [
    
    url(r'^', include(router.urls)), 
 
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 