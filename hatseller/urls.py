from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout')
]
