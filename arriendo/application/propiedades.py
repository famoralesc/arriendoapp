from django.shortcuts import render
from ..services import propiedades as propiedades_services
BASE_HTML_ROUTE = 'propiedades'

def index(request):
    html_route = 'index.html'
    return render(request, f"{BASE_HTML_ROUTE}/{html_route}", {'propiedades': propiedades_services.get_all()})

def create(request):
    pass

def update(request, id):
    pass

def delete(request, id):
    pass
