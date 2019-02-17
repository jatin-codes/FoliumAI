

from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
import settings as s
import sys

# set up settings
s.init(sys.argv)

from API_endpoints.Info_api import *


# LOCAL CONSTANTS, path to React app build and react app static folder

# 1. < !~-~-~~-~-~ FLASK ~-~-~~-~-~!> #

# Initialize Flask Framework with links to react builds
app = Flask(__name__)
CORS(app)
api = Api(app)

# serve the react app
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')


# 4. < !~-~-~~-~-~ API ENDPOINTS ~-~-~~-~-~!> #

api.add_resource(Info_api, '/api/info')

if __name__ == '__main__':
    app.run(debug=s.dev)