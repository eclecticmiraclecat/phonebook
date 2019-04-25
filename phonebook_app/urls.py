from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:name_id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('<int:name_id>/update/', views.update, name='update'),
    path('<int:name_id>/', views.read, name='read'),
]
