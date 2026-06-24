from django.urls import path
from django.contrib.auth import views
from . import views as my_views

urlpatterns = [
    path('', my_views.book_list, name='book_list'),
    path('<int:pk>/', my_views.book_detail, name='book_detail'),
    path('make/', my_views.book_create, name='book_create'),
    path('<int:pk>/change/', my_views.book_update, name='book_update'),
    path('<int:pk>/remove/', my_views.book_delete, name='book_delete'),
    
    path('register/', my_views.signup, name='signup'),
    path('signin/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signout/', my_views.logout_view, name='logout'),
]