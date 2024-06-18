from typing import List, Dict
from ..models import Propiedad

def get_all() -> List[Dict]:
    return [
        {
            "id": p.id,
            "rol": p.rol,
            "direccion": p.direccion,
            "dueno": p.dueno
        }
        for p in Propiedad.objects.all()
    ]

def get_by_id(id :int):
    return Propiedad.objects.get(pk=id)