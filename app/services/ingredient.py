from app.common.http_methods import GET, POST, PUT
from .base_service import BaseService
from flask import Blueprint, jsonify, request

from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)
service = BaseService(IngredientController)

@ingredient.route('/', methods=POST)
def create_ingredient():
   return service.create_entity()


@ingredient.route('/', methods=PUT)
def update_ingredient():
    return service.update_entity()
    

@ingredient.route('/id/<_id>', methods=GET)
def get_ingredient_by_id(_id: int):
   return service.get_entity_by_id(_id)


@ingredient.route('/', methods=GET)
def get_ingredients():
   return service.get_entities()