from flask import Flask
from .home.route import homeBp


app = Flask(__name__)

app.register_blueprint(homeBp)


