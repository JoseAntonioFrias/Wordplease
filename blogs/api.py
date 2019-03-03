from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from blogs.models import Blog
from blogs.permissions import BlogPermission
from blogs.serializers import BlogSerializer


class BlogListAPIView(ListAPIView):
    """
    ListAPIView: acción de listar los Blogs.
    """
    queryset = Blog.objects.all()
    permission_classes = [BlogPermission]
    serializer_class = BlogSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("owner__username",)
    ordering_fields = ("owner__first_name",)
