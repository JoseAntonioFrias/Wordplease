from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator
from django.shortcuts import render
from blogs.forms import BlogForm
from blogs.models import Blog
from django.contrib import messages
from django.views.generic import ListView

from commons.beautifulsoup_utils import generate_new_html_errors


class NewBlogView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = BlogForm()
        context = {'form': form}
        return render(request, 'blogs/new_blog.html', context)

    @method_decorator(login_required)
    def post(self, request):
        # Nos definimos previamente un formulario con el valor del usuario que hemos excluido de la página.
        new_blog_in = Blog(owner=request.user)

        # Coge los datos del formulario y de los ficheros
        form = BlogForm(request.POST, instance=new_blog_in)

        if form.is_valid():
            new_blog_in = form.save()
            messages.success(request, 'Blog {0} creado con éxito!'.format(new_blog_in.title))

            # Se limpia el formulario para una nueva inserción
            form = BlogForm()
        else:
            storage = generate_new_html_errors(form.errors)
            for msg in storage:
                messages.error(request, storage.get(msg))

        return render(request, 'blogs/new_blog.html', {'form': form})


class ListBlogs(ListView):
    model = Blog
    template_name = 'blogs/list_blogs.html'

    def get_queryset(self):
        result = super().get_queryset()
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['claim'] = 'List of user blogs'
        return context
