from django.contrib import admin
from django.urls import path
from arriendo.application.propiedades import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('propiedades/', index, name='index'), 
]
