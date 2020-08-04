"""B2B_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.api import Userlist, UserDetail
from seller.api import Sellerlist, SellerDetail
from product.api import Productlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/userlist/', Userlist.as_view(), name="user_list"),
    path('api/userdetail/<int:user_id>', UserDetail.as_view(), name="user_detail"),
    path('api/sellerlist', Sellerlist.as_view(), name="seller_list"),
    path('api/sellerdetail/<int:seller_id>', SellerDetail.as_view(), name="seller_detail"),
    path('api/productlist', Productlist.as_view(), name="product_list"),
]