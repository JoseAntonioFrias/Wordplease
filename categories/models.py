from django.db import models


class Category(models.Model):
    """
    Modelo que mapea la entidad Category de la BBDD.
    """
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
