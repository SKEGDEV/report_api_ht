from flask import Flask
from flask_cors import CORS
from os import getenv
from dotenv import load_dotenv
from src.routes.routes import routes

#Blueprints

server_api = Flask(__name__)
CORS(server_api)

#register Blueprint
server_api.register_blueprint(routes, url_prefix="/api")


if __name__ == '__main__':
    load_dotenv()
    server_api.run(host=getenv('host'), port=getenv('port'), debug=True)
