from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user_in_django, logout as finish_user_session
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect
from django.views import View

from commons.beautifulsoup_utils import generate_new_html_errors
from users.forms import LoginForm, SignupForm


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # comprobamos si el usuario esta dado de alta
            user = authenticate(username=username, password=password)

            if user is None:
                # Return an 'invalid login' error message. Porque no existe el usuario/password
                messages.error(request, 'Usuario o contraseña equivocado.')
            else:
                # Si el usuario existe tenemos que hacer login del usuario en la sesión
                login_user_in_django(request, user)

                # Si entro por primera vez autenticado me redirige a la página home.
                # Si no estoy logado y he accedido a través de la url a otra página y aparece en la url el parámetro
                # next. Si accedo ya logado aprovecha el querystring con el parámetro 'next' para redirigirme a la
                # página de origen de next.
                welcome_url = request.GET.get('next', 'home')

                # Redirige a la página de éxito.
                return redirect(welcome_url)

        context = {'form': form}
        return render(request, 'users/login.html', context)


class LogoutView(View):
    def get(self, request):
        finish_user_session(request)
        messages.success(request, 'La sesión se ha cerrado con éxito.')
        return redirect('login')


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        context = {'form': form}
        return render(request, 'users/signup.html', context)

    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            new_user = User()
            new_user.username = form.cleaned_data.get('username')
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.email = form.cleaned_data.get('email')
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()

            messages.success(request, 'Usuario registrado con éxito')
            form = SignupForm()
        else:
            storage = generate_new_html_errors(form.errors)
            for msg in storage:
                messages.error(request, storage.get(msg))

        return render(request, 'users/signup.html', {'form': form})
