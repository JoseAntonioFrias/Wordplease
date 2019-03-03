from django.urls import path
from media_uploader.api import MediaUploaderCreateAPIView

urlpatterns = [
    # API REST
    path('api/1.0/media_uploader/', MediaUploaderCreateAPIView.as_view(), name='api_media_uploader')
]
