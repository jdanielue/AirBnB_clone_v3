#!/usr/bin/python3
"""get the status of this page """
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"amenities": Amenity, "cities": City,
           "places": Place, "reviews": Review, "states": State, "users": User}


@app_views.route('/status', strict_slashes=False, methods=('GET',))
def get_status():
    """get the status of this page """
    mydict = {'status': 'OK'}
    return mydict


@app_views.route('/stats', strict_slashes=False, methods=('GET',))
def get_stats():
    """get the stats of storage """
    dict_stats = {}
    for clase, valor in classes.items():
        dict_stats[clase] = storage.count(valor)
    return dict_stats
