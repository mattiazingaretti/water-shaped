from flask import Blueprint, render_template

aboutBp = Blueprint('about', __name__)

@aboutBp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')