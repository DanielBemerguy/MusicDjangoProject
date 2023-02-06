from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.loginPage, name="login"),
     path('logout/', views.logoutUser, name="logout"),
     path('register/', views.registerPage, name="register"),
     path('', views.home, name="home"),
     path('band/<str:pk>', views.band, name="band"),
     path('music/<str:pk>', views.music, name="music"),
     path('create-band/', views.createBand, name="create-band"),
     path('update-band/<str:pk>', views.updateBand, name="update-band"),
     path('delete-band/<str:pk>', views.deleteBand, name="delete-band"),
     path('create-music/', views.createMusic, name="create-music"),
     path('update-music/<str:pk>', views.updateMusic, name="update-music"),
     path('delete-music/<str:pk>', views.deleteMusic, name="delete-music"),
     path('profile/<str:pk>', views.userProfile, name='user-profile'),
     path('delete-message/<str:pk>', views.deleteMessage, name="delete-message"),
]
