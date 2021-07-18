from django.urls import path, include
from .views import HomeView,BlogView,CreatePostView,UpdatePostView,DeletePostView,CreateCategoryView,DeleteCategoryView,EditCategoryView,CategoryView
from . import views
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('blog/<int:pk>',BlogView.as_view(),name='blog-detail'),
    path('createPost/',CreatePostView.as_view(),name='create-post'),
    path('blog/edit/<int:pk>',UpdatePostView.as_view(),name='update-post'),
    path('blog/delete/<int:pk>',DeletePostView.as_view(),name='delete-post'),
    path('editCategory/',EditCategoryView.as_view(),name='edit-cat'),
    path('addCategory/',CreateCategoryView.as_view(),name='add-cat'),
    path('delCategory/<int:pk>',DeleteCategoryView.as_view(),name='del-cat'),
    path('blog/category/<str:cat>',CategoryView,name='cat-view'),
]
