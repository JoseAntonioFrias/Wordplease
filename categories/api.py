from rest_framework import viewsets

from categories.models import Category
from categories.permissions import CategoryPermission
from categories.serializers import CategorySerializer, CategoryListSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet: acciones a realizar ( CRUD ) sobre el modelo Category.
    """
    permission_classes = [CategoryPermission]
    queryset = Category.objects.all()

    def get_serializer_class(self):
        return CategoryListSerializer if self.action == 'list' else CategorySerializer
