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
    return jsonify(current_state.cities)

    """
    list_todict = []
    dict_instances = storage.all(City)
    id_name = "City." + str(city_id)
    error_dict = {"error": "Not found"}
    if request.method == 'GET':
        if city_id is None:
            for element in dict_instances:
                list_todict += [dict_instances[element].to_dict()]
        elif id_name in dict_instances:
            list_todict += [dict_instances[id_name].to_dict()]
        else:
            mydict = {"error": "Not found"}
            return error_dict, 404
        return jsonify(list_todict)
    elif request.method == 'DELETE':
        if id_name in dict_instances:
            obj = storage.get(City, city_id)
            storage.delete(obj)
            storage.save()
            return {}, 200
        else:
            return error_dict, 404
    elif request.method == 'POST':
        try:
            header_dict = request.get_json()
            if 'name' not in header_dict:
                return "Missing name", 400
        except:
            return "Not a JSON", 400
        new_city = City(**header_dict)
        new_city.save()
        return new_city.to_dict(), 201
    elif request.method == 'PUT':
        if id_name not in dict_instances:
            return error_dict, 404
        try:
            header_dict = request.get_json()
        except:
            return "Not a JSON", 400
        to_update = storage.get(City, city_id)
        for element, value in header_dict.items():
            if element not in ['id', 'created_at', 'updated_at']:
                setattr(to_update, element, value)
        storage.save()
        return to_update.to_dict(), 201"""
