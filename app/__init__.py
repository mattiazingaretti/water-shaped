from flask import Flask
from .home.route import homeBp
from .projects.route import projBp
from .contact.route import contBp
from .articles.route import artBp 
from .about.route import aboutBp


app = Flask(__name__)

app.register_blueprint(homeBp)
app.register_blueprint(projBp)
app.register_blueprint(contBp)
app.register_blueprint(artBp)
app.register_blueprint(aboutBp)


