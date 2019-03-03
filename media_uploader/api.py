from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from media_uploader.models import Media
from media_uploader.serializers import MediaUploaderSerializer


class MediaUploaderCreateAPIView(generics.CreateAPIView):
    """
    CreateAPIView: acción para subir al servidor una imagen o video.
    """
    queryset = Media.objects.all()
    serializer_class = MediaUploaderSerializer
    # Sólo usuarios autenticados
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
