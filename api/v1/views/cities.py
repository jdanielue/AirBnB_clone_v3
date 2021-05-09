#!/usr/bin/python3
"""
City objects that handles all default RestFul API actions
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


@app_views.route('/states/<state_id>/cities', strict_slashes=False,
                 methods=('GET', 'DELETE', 'POST', 'PUT'))
@app_views.route('/states/<state_id>/cities/<city_id>', strict_slashes=False,
                 methods=('GET', 'DELETE', 'POST', 'PUT'))
def get_city(city_id=None, state_id=None):
    current_state = storage.get(State, state_id)
    error_dict = {"error": "Not found"}
    if request.method == 'GET':
        if current_state is not None:
            list_cities = map(lambda x: x.to_dict(), current_state.cities)
            return jsonify(list(list_cities))
        else:
            return error_dict, 404
    elif request.method == 'POST':
        try:
            header_dict = request.get_json()
            if 'name' not in header_dict:
                return "Missing name", 400
        except:
            return "Not a JSON", 400
        header_dict['state_id'] = state_id
        new_city = City(**header_dict)
        new_city.save()
        return new_city.to_dict(), 201


@app_views.route('/cities/<city_id>', strict_slashes=False,
                 methods=('GET', 'DELETE', 'POST', 'PUT'))
def get_city_no_state(city_id=None):
    """This function retrieves a city"""
    current_city = storage.get(City, city_id)
    error_dict = {"error": "Not found"}

    if request.method == 'GET':
        if current_city is not None:
            return current_city.to_dict()
        else:
            return error_dict, 404
    elif request.method == 'DELETE':
        obj = storage.get(City, city_id)
        if obj is not None:
            storage.delete(obj)
            storage.save()
            return {}, 200
        else:
            return error_dict, 404
    elif request.method == 'PUT':
        obj = storage.get(City, city_id)
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
