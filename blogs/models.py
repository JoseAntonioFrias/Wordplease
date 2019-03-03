from django.contrib.auth.models import User
from django.db import models


class Blog (models.Model):
    """
    Modelo que mapea la entidad Blog de la BBDD.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
