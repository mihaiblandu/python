"""trydjango URL Configuration

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
from pages.views import social_view, contact_view, about_view, service_view
from products.views import product_detail_view , product_view , product_list , product_create_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", social_view),
    path("contact", contact_view),
    path("about", about_view),
    path("service", service_view),
    path("product", product_detail_view),
    path("products", product_view),
    path("allproducts", product_list),
    path('create/', product_create_view),
]
