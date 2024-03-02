from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about/', views.about_page, name='about_page'),
    path('apply/', views.apply_login, name='apply_login'),
    path('signup/', views.apply_signup, name='apply_signup'),
    path('home/', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('logout/', views.logoutpage, name='logout'),

]
