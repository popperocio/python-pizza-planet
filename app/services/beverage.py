from app.common.http_methods import POST, PUT, GET
from .base_service import BaseService
from flask import Blueprint, jsonify, request

from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)
service = BaseService(BeverageController)

@beverage.route('/', methods=POST)
def create_beverage():
    return service.create_entity()


@beverage.route('/', methods=PUT)
def update_beverage():
    return service.update_entity()


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return service.get_entity_by_id(_id)


@beverage.route('/', methods=GET)
def get_beverages():
    return service.get_entities()
