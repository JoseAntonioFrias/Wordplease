from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from users.permissions import UserPermission
from users.serializers import UserSerializer


class UserDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateDestroyAPIView: acciones de consultar, modificar y eliminar un usuario.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]


class CreateUserAPIView(CreateAPIView):
    """
    CreateAPIView: acción de crear un usuario.
    """
    serializer_class = UserSerializer
