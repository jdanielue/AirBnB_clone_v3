#!/usr/bin/python3
"""
review objects that handles all default RestFul API actions
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


@app_views.route('/places/<place_id>/reviews', strict_slashes=False,
                 methods=('GET', 'DELETE', 'POST', 'PUT'))
def get_review(place_id=None):
    current_place = storage.get(Place, place_id)
    error_dict = {"error": "Not found"}
    list_places = []
    if request.method == 'GET':
        if current_place is not None:
            for llave, valor in storage.all(Review).items():
                if place_id in valor.to_dict().values():
                    list_places += [valor.to_dict()]
            if len(list_places) != 0:
                return jsonify(list_places)
        return error_dict, 404


@app_views.route('/places/<place_id>/reviews/<review_id>',
                 strict_slashes=False,
                 methods=('GET', 'DELETE', 'POST', 'PUT'))
def get_list_review(place_id=None, review_id=None):
    current_place = storage.get(Place, place_id)
    current_review = storage.get(Review, review_id)
    error_dict = {"error": "Not found"}
    list_places = []
    if request.method == 'GET':
        if current_place is not None and current_review is not None:
            for llave, valor in storage.all(Review).items():
                if review_id in valor.to_dict().values():
                    return valor.to_dict()
        return error_dict, 404
    elif request.method == 'DELETE':
        current_review = storage.get(Review, review_id)
        if current_review is not None:
            storage.delete(current_review)
            storage.save()
            return {}, 200
        else:
            return error_dict, 404
    elif request.method == 'POST':
        header_dict = request.get_json()
        if storage.get(Place, header_dict["place_id"]) is None:
            return error_dict, 404
        try:
            header_dict = request.get_json()
        except:
            return "Not a JSON", 400
        if 'name' not in header_dict:
            return "Missing name", 400
        if 'user_id' not in header_dict:
            return "Missing user_id", 400
        if 'text' not in header_dict:
            return "Missing text", 400
        if storage.get(User, header_dict["user_id"]) is None:
            return error_dict, 404
        else:
            new_review = Review(**header_dict)
            new_review.save()
            return new_review.to_dict(), 201
    elif request.method == 'PUT':
        current_review = storage.get(Review, review_id)
        if current_review is None:
            return error_dict, 404
        try:
            header_dict = request.get_json()
        except:
            return "Not a JSON", 400
        for llave, value in header_dict.items():
            if llave not in ["id", "user_id", "place_id",
                             "created_at", "updated_at"]:
                setattr(current_review, llave, value)
        storage.save()
        return current_review.to_dict(), 201
