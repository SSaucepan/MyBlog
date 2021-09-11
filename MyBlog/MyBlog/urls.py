"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from MyBlog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #首页
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('index11/', views.index11, name='index11'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('about_me/', views.about_me, name='about_me'),
]
