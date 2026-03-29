from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.home, name='home'),
    path('advertisement_like/<int:pk>', views.advertisement_like, name="advertisement_like"),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    #path('update_user/', views.update_user, name='update_user'),
]