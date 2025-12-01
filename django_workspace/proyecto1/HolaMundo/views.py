from django.shortcuts import render
from django.http import HttpResponse # necesario para responder al cliente
# con httpresponse se puede responder con texto plano o HTML

# Create your views here.

# forma de responder al cliente cuando hace un http
def hola_mundo (request): # el request captura las peticiones de los clientes
    return HttpResponse ("<h1>hola mundo</h1>")
# con esto hemos habilitado una vista, pero hay que además enlazar el proyecto con la
# aplicación

def home (request): # pinta una página con render, también hay que darlo de alta en urls.py
    return render(request,'index.html') # la página index.html hay que crearla dentro del
# archivo de configuración de todo proyecto de django, settings.py