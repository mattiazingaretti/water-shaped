from flask import Blueprint,render_template, jsonify, request, redirect,url_for , flash
from app.contact.utils import   setMessage, sendEmail

contBp = Blueprint("cont", __name__)

@contBp.route('/contact', methods=['GET','GET'])
def contact():

    return render_template('contact.html')


@contBp.route('/sendMsg', methods=['POST'])
def sendMsg():
    if request.method == "POST":
        #Fancy not empty security check
        f_name = request.form.get("first_name")
        l_name = request.form.get("last_name")
        subject = request.form.get("subject")
        msg = request.form.get("msg")
        if f_name and l_name and subject and msg:
            msg = setMessage(str(f_name +" "+ l_name) , str(subject), str(msg))
            status = sendEmail(msg)
            if status == 0:
                flash("Message sent successfully ! ",'success')
            else:
                flash("Message not sent, service unavailable ",'error')
        return redirect(url_for('cont.contact'))
    else:
        flash("Error while sending message",'error')
        return jsonify({"error":"wrong request method"}),500 
    
