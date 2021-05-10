#!/usr/bin/python3
"""
Place objects that handles all default RestFul API actions
"""

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from flask import jsonify, request


@app_views.route('/cities/<city_id>/places', strict_slashes=False,
                 methods=('GET', 'DELETE', 'POST', 'PUT'))
@app_views.route('/cities/<city_id>/places/<place_id>', strict_slashes=False,
                 methods=('GET', 'DELETE', 'POST', 'PUT'))
def get_place(place_id=None, city_id=None):
    current_city = storage.get(City, city_id)
    error_dict = {"error": "Not found"}
    list_places = []
    if request.method == 'GET':
        if current_place is not None:
            for llave, valor in storage.all(Cities).items():
                if place_id in valor.to_dict().values():
                    list_places += [valor.to_dict()]
            if len(list_places) != 0:
                return jsonify(list_places)
        return error_dict, 404
    elif request.method == 'POST':
        header_dict = request.get_json()
        if storage.get(City, header_dict["city_id"]) is None:
            return error_dict, 404
        try:
            header_dict = request.get_json()
            if 'name' not in header_dict:
                return "Missing name", 400
            if 'user_id' not in header_dict:
                return "Missing user_id", 400
        except:
            return "Not a JSON", 400
        if storage.get(User, header_dict["user_id"]) is None:
            return error_dict, 404
        else:
            new_place = Place(**header_dict)
            new_place.save()
            return new_place.to_dict(), 201


@app_views.route('/places/<place_id>', strict_slashes=False,
                 methods=('GET', 'DELETE', 'POST', 'PUT'))
def get_place_no_city(place_id=None):
    """This function retrieves a place"""
    current_place = storage.get(Place, place_id)
    error_dict = {"error": "Not found"}

    if request.method == 'GET':
        if current_place is not None:
            return current_place.to_dict()
        else:
            return error_dict, 404
    elif request.method == 'DELETE':
        obj = storage.get(Place, place_id)
        if obj is not None:
            storage.delete(obj)
            storage.save()
            return {}, 200
        else:
            return error_dict, 404
    elif request.method == 'PUT':
        obj = storage.get(Place, place_id)
        if obj is None:
            return error_dict, 404
        try:
            header_dict = request.get_json()
        except:
            return "Not a JSON", 400
        for element, value in header_dict.items():
            if element not in ['id', 'created_at', 'updated_at']:
                setattr(obj, element, value)
        storage.save()
        return obj.to_dict(), 201
