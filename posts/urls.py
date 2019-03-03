"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.api import PostViewSet
from posts.views import HomeView, NewPostView, ListPostsView, PostDetailView

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/new_post', NewPostView.as_view(), name='new_post'),
    path('blogs/<str:username>/<int:blog_id>', ListPostsView.as_view(), name='list_posts'),
    path('posts/<int:post_id>', PostDetailView.as_view(), name='detail_post'),

    # API REST
    path('api/1.0/', include(router.urls))
]
