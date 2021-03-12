from flask import Blueprint, render_template

bioBp = Blueprint('bio', __name__)

@bioBp.route('/bio', methods=['GET'])
def bio():
    return render_template('bio.html')