from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='focus-home' ),
    path('about/', views.about,name='focus-about')
    # path('register/', views.register,name='focus-register')
]
