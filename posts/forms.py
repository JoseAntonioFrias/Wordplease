from django import forms
from django.conf import settings
from django.forms import ModelForm
from commons.utils import get_extension_file
from posts.models import Post


class PostForm (ModelForm):

    class Meta:
        model = Post
        fields = ['blog', 'title', 'summary', 'body', 'image', 'video', 'categories', 'pub_date']
        labels = {
            'blog': 'Blog',
            'title': 'Título',
            'summary': 'Introducción',
            'body': 'Contenido',
            'image': 'Fichero multimedia: imagen o video',
            'video': 'Video',
            'categories': 'Categorías',
            'pub_date': 'Fecha de publicación'
        }
        widgets = {
            'blog': forms.Select(attrs={'class': 'custom-select', 'selected': 'Seleccione una opción'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del post'}),
            'summary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Introducción del post'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenido del post'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'defaultValue:': 'Seleccione una imagen'}),
            'video': forms.FileInput(attrs={'class': 'form-control-file', 'defaultValue:': 'Seleccione un video'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control', 'id': 'datetimepicker1',
                                                   'format': '%d/%m/%Y %H:%M:%S'})
        }
        exclude = ['owner']

    def clean(self):
        cleaned_data = super().clean()
        image_file = cleaned_data.get('image', None)
        image_file_extension = get_extension_file(image_file.name)

        if image_file_extension in settings.VALID_VIDEO_EXTENSIONS:
            cleaned_data["image"] = None
            cleaned_data["video"] = image_file

        return cleaned_data
