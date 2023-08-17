from src.utils.bcrypt import bcrypt
from functools import wraps
from flask import request, jsonify
from os import getenv
import json

class auth_decorator():
    
    def verify_auth(self):  
        o_request = json.loads(request.get_json())
        try:
            if(not o_request['oauth']):
                return{
                        "msm":"UNAUTHORIZED",
                        "err":"Objeto de autorizacion no encontrado, por favor intente nuevamente"
                        }
            o_usr = o_request['oauth']['usr']
            o_pass = o_request['oauth']['pass'] 
            usr = getenv("api_usr")
            pss = getenv("api_pss")
            if(not bcrypt().match(str(usr), o_usr) or not bcrypt().match(str(pss), o_pass)):
                return{
                        "msm":"UNAUTHORIZED",
                        "err":"El usuario o la contrasena no son correctos, por favor verifique su autenticacion"
                        }
            return {"success":"AUTHORIZE"} 
        except Exception as e:
            return{
                    "msm":"UNAUTHORIZED",
                    "err":str(e)
                    }

    def auth_isRequired(self, f):
        @wraps(f)
        def decorator(*args, **kwargs):
            res = self.verify_auth()
            if(not res.get('success')):
                response = jsonify(res)
                response.status_code=401
                return response
            return f( *args, **kwargs) 
        return decorator
