"""talk_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blog.views import (
    post_list, 
    get_post, 
    create_post,
    update_post,
    delete_post,
)
    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list),
    path('single-post/<pk>/', get_post, name='single-post'),
    path('create-post/', create_post, name='create-post'),
    path('single-post/<pk>/edit-post/', update_post, name='edit-post'),
    path('single-post/<pk>/delete-post/', delete_post, name='delete'),
]
    