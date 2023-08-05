from flask import Blueprint, jsonify, request
from src.utils.validator import auth_decorator

routes = Blueprint('routes', __name__)

@routes.route("/get-qualification", methods=['POST'])
@auth_decorator().auth_isRequired
def qualification():
    o_request = request.get_json()
    return jsonify({
        "msm":"prueba exitosa"
        })

