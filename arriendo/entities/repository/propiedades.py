from ..models import Propiedad

def get_all():
    return Propiedad.objects.all()

def get_by_id(id :int):
    return Propiedad.objects.get(pk=id)