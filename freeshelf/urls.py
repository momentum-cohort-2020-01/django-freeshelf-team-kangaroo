"""freeshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from core import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.books_list, name='books-list'),
    path('books/<int:pk>/', views.books_details, name = 'books-details'),
    path('books/new/', views.books_new, name='books-new'),
    path('admin/', admin.site.urls),
    path('book/<int:pk>/edit/', views.books_edit, name = 'books-edit'),
    path('book/<int:pk>/delete/', views.books_delete, name = 'books-delete'),
    path('books/<slug:slug>/', views.tagged, name= 'books-by-tag'),
    path('book/<int:pk>/like/', views.books_liked, name = 'books-like'),
    path('book/<int:pk>/dislike/', views.books_disliked, name = 'books-dislike'),
    path('accounts/', include('registration.backends.default.urls')),
]
