from django.contrib.auth.models import User
from django.db import models
from commons.validators import validate_file_type


class Media (models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    media_name = models.FileField(upload_to='api_uploader', null=True, blank=True, validators=[validate_file_type])
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __unicode__(self,):
        return str(self.media_name)


