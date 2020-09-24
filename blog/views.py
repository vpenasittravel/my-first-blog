from django.shortcuts import render

#request peticiones recibidas desde el navegador del cliente
#render para construir la plantilla html
#{} todos los argumentos que nosotros enviamos a la template del cliente en formato json
#"contruyeme la plantilla con este request que recibimos y con estos argumentos/parametros que te envío"


def post_list(request):
    return render(request, 'blog/post_list.html', {'nombre' : 'vicky'})