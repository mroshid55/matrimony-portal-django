from django.urls import path,include
from .import views
urlpatterns = [
    path('all-people/', views.all_people, name='all-people'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('followers/<int:pk>',views.followers,name='followers'),
    path('following/<int:pk>',views.following,name='following'),
    path('update-profile',views.updateprofile,name='update-profile'),
    ##################################### Chat ######################################
    path('friend/<str:pk>', views.detail, name="detail"),
    path('sent_msg/<str:pk>', views.sentMessages, name = "sent_msg"),
    path('rec_msg/<str:pk>', views.receivedMessages, name = "rec_msg"),
    ##################################### Chat ######################################
    path('all-notifications',views.allnotifications,name='all-notifications'),
    path('notifications-delete/<int:pk>/',views.deletenotifications,name='notifications-delete'),
]