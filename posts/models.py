import os
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from blogs.models import Blog
from categories.models import Category
from commons.utils import get_extension_file
from commons.validators import validate_file_type


class Post(models.Model):
    """
    Modelo que mapea la entidad Post de la BBDD.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.TextField(max_length=80, unique=True)
    summary = models.TextField(max_length=200, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True, validators=[validate_file_type])
    video = models.FileField(null=True, blank=True, validators=[validate_file_type])
    categories = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(default=timezone.now)
    last_modification = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def get_categories(self):
        return ",".join([str(c.name) for c in self.categories.all()])

    def get_video_extension(self):
        if self.video:
            file_path = self.video.name
            return get_extension_file(file_path)

    def __str__(self):
        return 'Author: {0} Title: {1} '.format(self.owner, self.title)


