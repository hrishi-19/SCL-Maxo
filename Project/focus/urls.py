from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    # PostUploadView
)
from . import views

urlpatterns = [
    path('home/', views.home,name='focus-home' ),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('post/<int:pk>/upload/', PostUploadView.as_view(), name='post-upload'),
    # path('user/<str:username>/', views.profiledetail, name='profiledetail'),
    path('', views.infopage, name='focus-infopage'),
    path('about/', views.about, name='focus-about')
]
