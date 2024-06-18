from typing import Dict, List
from ..entities.repository import propiedades as propiedades_repository

def get_all() -> List[Dict]:
    return propiedades_repository.get_all()

def get_by_id(id: int) -> Dict:
    pass