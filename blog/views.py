from django.shortcuts import render
from django.utils import timezone
from .models import Post
"""
El punto antes de models indica el directorio actual o la aplicación actual.
Ambos, views.py y models.py están en el mismo directorio.
Esto significa que podemos utilizar . y el nombre del archivo (sin .py). Ahora importamos el nombre del modelo (Post)."""

#request peticiones recibidas desde el navegador del cliente
#render lo utilizamos para indicar que se va a pintar una plantilla html
#{} todos los argumentos que nosotros enviamos a la template del cliente en formato json
#"contruyeme la plantilla con este request que recibimos y con estos argumentos/parametros que te envío"
#Las views conectan modelos con plantillas. 


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})