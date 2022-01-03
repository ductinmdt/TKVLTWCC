from django.urls import path,include
from .views import *
from django.conf import settings
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'adminproduct', AdminProductView)

urlpatterns = [
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', register,name='register'),
    path('login/', login,name='login'),
    path('logout/', logout,name='logout'),
    path('user/', userview,name='user'),
    path('cart/',CartdetailsView,name='cart'),
    path('products/', ProductView,name='products'),
    path('addtocart/',Addtocart,name='addtocart'),
    path('products/<str:code>/', ProductbycodeView,name='productbycode'),
    path('productsfilter/', Productfilter,name='productfilter'),
    path('brand/', BrandView,name='brand'),
    path('newproducts/', NewProductView,name='newproducts'),
    path('instockproducts/', instockProductView,name='instockproducts'),
    path('hotproducts/', HotProductView,name='hotproducts'),
    path('checkout/',Checkout,name='checkout'),
    path('changecartdetails/',changecartdetails,name='changecart'),
    path('adminorderview/',AdminOrderView,name='adminorderview'),
    # path("", include(router.urls)),
    path('productadminview/',productadminview,name='productadminview'),
    path('orders/', OrdersView,name='orders'),
]