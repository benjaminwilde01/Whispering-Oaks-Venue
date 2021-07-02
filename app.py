from flask import Flask, jsonify, g
from flask_cors import CORS
from peewee import Ordering

import models
from resources.whispering_oaks import visitor

DEBUG = True
PORT = 5000

print(__name__)
app = Flask(__name__)


@app.before_request
# Connect to the database before each request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
# Close the database connection after each request
def after_request(response):
    g.db.close()
    return(response)


@app.route('/') 
def index():
    return 'Hello from Flask'


CORS(visitor, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(visitor, url_prefix='/api/v1/whispering_oaks')


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)