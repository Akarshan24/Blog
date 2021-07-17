from django.urls import path, include
from .views import HomeView,BlogView,CreatePostView,UpdatePostView,DeletePostView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('blog/<int:pk>',BlogView.as_view(),name='blog-detail'),
    path('createPost/',CreatePostView.as_view(),name='create-post'),
    path('blog/edit/<int:pk>',UpdatePostView.as_view(),name='update-post'),
    path('blog/delete/<int:pk>',DeletePostView.as_view(),name='delete-post')
]
