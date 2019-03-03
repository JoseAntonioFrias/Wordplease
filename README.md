# Wordplease

Práctica del módulo de Python y Django del bootcamp de Desarrollo Web de Keepcoding.

---

## Instalación
Es necesario tener instalado Python 3 en el ordenador.


## Arrancar el entorno virtual env

```
virtualenv env -p python3
```

## Activar el entorno virtual env

```
source env/bin/activate
```

## Instalación de las dependencias del proyecto.

```
pip install -r requirements.txt
```

## Crea la estructura de tablas en la base de datos por defecto especificada en settings.py 

```
python manage.py migrate
```

## Creación de un usuario administrador.

```
python manage.py createsuperuser
```

### Arrancar el servidor web.

```
python manage.py runserver
```

---

## URLS del sitio Web

URL base: http://127.0.0.1:8000

| URL | Acción |
| ------- | --- |
| ```/``` | Página Home. Lista de los 10 últimos posts publicados. |
| ```/admin``` | Página de administración de la aplicación. |
| ```/login``` | Login. |
| ```/signup``` | Formulario de registro de un nuevo usuario. |
| ```/logout``` | Logout. |
| ```/blogs``` | Lista de blogs existentes. |
| ```/blogs/new_blog``` | Alta de un blog. |
| ```/posts/new_post``` | Alta de un post en un blog. |
| ```blogs/<str:username>/<int:blog_id>``` | Lista de posts publicados por un usuario en un blog. |
| ```posts/<int:post_id>``` | Detalle de un post. |

---

## API REST

### Users

| URL | Método HTTP | Acción |
| --- | --- | --- |
| ```/api/1.0/users/``` | GET | Lista de usuarios. |
| ```/api/1.0/users/``` | POST | Alta de un usuario. |
| ```/api/1.0/users/<id>/``` | GET | Detalle de un usuario. |
| ```/api/1.0/users/<id>/``` | PUT | Modificación de un usuario. |
| ```/api/1.0/users/<id>/``` | DELETE | Borrado de un usuario. |


### Blogs

| URL | Método HTTP | Acción |
| --- | --- | --- | 
| ```/api/1.0/blogs/``` | GET | Lista de blogs. |


### Posts

| URL | Método HTTP | Acción |
| --- | --- | --- |
| ```/api/1.0/users/``` | GET | Lista de posts. |
| ```/api/1.0/users/``` | POST | Alta de un post. |
| ```/api/1.0/users/<id>/``` | GET | Detalle de un post. |
| ```/api/1.0/users/<id>/``` | PUT | Modificación de un post. |
| ```/api/1.0/users/<id>/``` | DELETE | Borrado de un post. |


### Media Uploader

| URL | Método HTTP | Acción |
| --- | --- | --- |
| ```/api/1.0/media_uploader/``` | POST | Cargador multimedia de imágenes y videos. |

