from django.urls import path
from Blogg import views
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView
)

urlpatterns = [
    path('',PostListView.as_view(), name ='Blogg-entry'),
    path('post/<int:pk>/',PostDetailView.as_view(), name ='post-detail'),
    path('post/new/',PostCreateView.as_view(), name ='post-create'), 
    path('about/', views.about, name = 'Blogg-about'),
    
]