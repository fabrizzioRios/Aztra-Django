from django.urls import path
from blog.views import PostListCreateView, PostRetrieveUpdateDestroyView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
]
