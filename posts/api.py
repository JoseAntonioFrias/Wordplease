from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostSerializer, PostListSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    Viewsets: acciones a realizar sobre el modelo Post.
    """
    queryset = Post.objects.all().order_by('-pub_date')
    permission_classes = [PostPermission]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'summary', 'body']
    ordering = ['title', 'pub_date']
    filter_fields = ['categories']

    def get_queryset(self):
        return self.queryset.filter(pub_date__lte=timezone.now()) if self.action == 'list' and not self.request.user.\
            is_authenticated else self.queryset.filter

    def get_serializer_class(self):
        return PostListSerializer if self.action == 'list' else PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
