from flask import Blueprint, render_template

projBp = Blueprint( "proj",__name__)


@projBp.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')


@projBp.route('/watershaped', methods=['GET'])
def watershaped():
    return render_template('projects/watershaped.html')
