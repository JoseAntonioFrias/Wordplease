from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView

from blogs.models import Blog
from categories.models import Category
from commons.beautifulsoup_utils import generate_new_html_errors
from posts.forms import PostForm
from posts.models import Post
from project.settings import PAGINATE_LIST_BY


class HomeView(ListView):
    model = Post
    template_name = 'posts/home.html'
    paginate_by = PAGINATE_LIST_BY

    # Seleccionamos los 10 últimos post añadidos.
    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]


class NewPostView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'posts/new_post.html', context)

    @method_decorator(login_required)
    def post(self, request):
        # Nos definimos previamente un formulario con el valor del usuario que hemos excluido de la página.
        new_post_in = Post(owner=request.user)

        # Coge los datos del formulario y de los ficheros
        form = PostForm(request.POST, request.FILES, instance=new_post_in)

        if form.is_valid():
            new_blog_in = form.save()
            messages.success(request, 'El post: {0} ha sido creado con éxito.'.format(new_post_in.title))

            # Se limpia el formulario para una nueva inserción
            form = PostForm()
        else:
            storage = generate_new_html_errors(form.errors)
            for msg in storage:
                messages.error(request, storage.get(msg))

        return render(request, 'posts/new_post.html', {'form': form})


class ListPostsView(ListView):
    model = Post
    template_name = 'posts/list_posts.html'
    paginate_by = PAGINATE_LIST_BY

    def get_queryset(self):
        username = self.kwargs.get('username', None)
        p_blog = self.kwargs.get('blog_id', None)
        p_category = self.request.GET.get('category', None)
        user = get_object_or_404(User, Q(username=username))
        result = super().get_queryset()

        if p_category is None or p_category == '0':
            return result.filter(owner=user.id, blog=p_blog, pub_date__lte=timezone.now()).order_by('-pub_date')
        else:
            return result.filter(owner=user.id, blog=p_blog, categories=p_category, pub_date__lte=timezone.now()).\
                order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['username'] = self.kwargs.get('username', None)

        blog_id = self.kwargs.get('blog_id', None)
        context['blog_id'] = blog_id
        blog = Blog.objects.get(id=blog_id)
        context['blog_title'] = blog.title

        p_category = self.request.GET.get('category', None)
        # opción seleccionada del combo
        context['category_selected'] = p_category
        # mensajes cuando no hay valores para una búsqueda por categoría
        context['btn_search_clicked'] = int(self.request.GET.get('btnSearch', '0'))

        if p_category is not None and p_category != '0':
            context['name_category'] = Category.objects.get(pk=p_category)
        elif p_category is not None and p_category == '0':
            context['name_category'] = 'Todas'
        return context


class PostDetailView(View):
    def get(self, request, post_id):
        try:
            post_detail = Post.objects.select_related().get(pk=post_id)

        except post_detail.DoesNotExist:
            # si no existe el post, devolvemos un 404
            messages.error(request, 'No existe el post, status 404')
            return HttpResponse('No existe el post.', status=404)

        context = {'post': post_detail}

        # devolver la respuesta utilizando una plantilla
        return render(request, 'posts/detail_post.html', context)
