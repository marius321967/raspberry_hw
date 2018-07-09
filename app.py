import os
from flask import Flask
from routes import register

app = Flask('hello_world')

register(app)

app.run(port=8080, host='0.0.0.0')
