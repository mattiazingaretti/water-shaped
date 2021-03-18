from flask import Blueprint,render_template


contBp = Blueprint("cont", __name__)

@contBp.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@contBp.route('/sendMsg', methods=['POST'])
def sendMsg():
