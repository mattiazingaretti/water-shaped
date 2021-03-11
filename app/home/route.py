from flask import Blueprint, redirect, redirect, render_template, url_for

homeBp = Blueprint(name="home",import_name= __name__)

@homeBp.route('/')
def index():
    return redirect(url_for('home.home'))

@homeBp.route('/home')
def home():
    return render_template('home.html')
    
