from app.common.http_methods import POST, PUT, GET
from flask import Blueprint, jsonify, request

class BaseService:
    
    def __init__(self, controller):
        self.controller = controller
    
    def create_entity(self):
        entity, error = self.controller.create(request.json)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    
    
    def update_entity(self):
        entity, error = self.controller.update(request.json)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    
        
    def get_entity_by_id(self, _id):
        entity, error = self.controller.get_by_id(_id)
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code


    def get_entities(self):
        entities, error = self.controller.get_all()
        response = entities if not error else {'error': error}
        status_code = 200 if entities else 404 if not error else 400
        return jsonify(response), status_code
