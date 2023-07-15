from app.common.http_methods import GET, POST, PUT
from .base_service import BaseService
from flask import Blueprint, jsonify, request

from ..controllers import SizeController

size = Blueprint('size', __name__)
service = BaseService(SizeController)

@size.route('/', methods=POST)
def create_size():
    return service.create_entity()


@size.route('/', methods=PUT)
def update_size():
    return service.update_entity()


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return service.get_entity_by_id(_id)


@size.route('/', methods=GET)
def get_sizes():
    return service.get_entities()

