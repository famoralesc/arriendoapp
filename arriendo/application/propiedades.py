from django.shortcuts import render

BASE_HTML_ROUTE = 'propiedades'

def index(request):
    html_route = 'index.html'
    return render(request, f"{BASE_HTML_ROUTE}/{html_route}", {'propiedades': []})