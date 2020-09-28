from django.shortcuts import render, get_object_or_404 , get_list_or_404
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
    #posts = get_list_or_404( Post, published_date__lte=timezone.now()) #en teoría con esta función si se recupera una lista vacía de posts, muestra la pag. 404
    args = {} #declaro diccionario
    args['posts'] = posts #creo y añado una key  al diccionario
    return render(request, 'blog/post_list.html', args) #envío el diccionario como argumentos

def post_detail(request, pk):
    #post = Post.objects.get(pk = pk)
    post = get_object_or_404(Post, pk=pk) #esta función me pinta la página 404 en caso de que el id que se envíe no exista
    posts = get_list_or_404(Post, published_date__lte=timezone.now()) #en esta variable envío todos los objetos de tipo Post para pintarlos en base.html
    args = {'post': post, 'posts':posts}
    return render(request, 'blog/post_detail.html', args)
    