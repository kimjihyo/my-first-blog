"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views

app_name = 'post'

urlpatterns = [
    path('<int:page_num>', views.postpage, name='postpage'),
    path('AddNewPost/', views.AddNewPost.as_view(), name='AddNewPost'),
    path('ViewPost/<int:pk>', views.DetailView.as_view(), name="ViewPost"),
    path('Search/<int:page_num>', views.SearchPost, name='SearchPost'),
    path('DeletePost/<int:pk>', views.DeletePost.as_view(), name='DeletePost'),
    path('UpdatePost/<int:pk>', views.UpdatePost.as_view(), name='UpdatePost'),
]
