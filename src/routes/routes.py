from flask import Blueprint, jsonify, request
from src.utils.validator import auth_decorator
from src.o_routes.o_rpt import o_rpt
import json

routes = Blueprint('routes', __name__)

@routes.route("/generate-rpt", methods=['POST'])
@auth_decorator().auth_isRequired
def qualification(): 
    o_request = json.loads(request.get_json())
    o_response = o_rpt(o_request).generateRpt() 
    response = jsonify(o_response)
    response.status_code = 200
    if(o_response.get("err")):
        response.status_code = 403
    return response

