from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.register, name='register'), 
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('bos/', views.bos, name='bos'),
    path('acaunt/', views.acaunt, name='acaunt'),
    path('logout/', views.logout, name='logout'),
    path('about/', views.about, name='about'),
    path('haqida/', views.haqida, name='haqida'),
    path('index/', views.index, name='index'),
    path('job/', views.job, name='job'),
    path('see/', views.see, name='see'),
    path('frontend/', views.frontend, name='frontend'),
    path('til/', views.til, name='til'),
]