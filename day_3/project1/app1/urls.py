from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books),
    path('<int:id>/', views.show_book),
    path('<int:id>/delete/', views.delete_book),
    path('add/', views.add_book)
]