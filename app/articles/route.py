from flask import Blueprint, render_template

artBp = Blueprint('art', __name__)

@artBp.route('/articles', methods=['GET'])
def articles():
    return render_template('articles.html')