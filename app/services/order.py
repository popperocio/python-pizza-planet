from app.common.http_methods import GET, POST
from .base_service import BaseService
from flask import Blueprint, jsonify, request

from ..controllers import OrderController

order = Blueprint('order', __name__)
service = BaseService(OrderController)

@order.route('/', methods=POST)
def create_order():
    return service.create_entity()


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return service.get_entity_by_id(_id)


@order.route('/', methods=GET)
def get_orders():
    return service.get_entities()
