# wsapp/routes.py
from flask import Blueprint, render_template

# Create a blueprint named 'main'
main = Blueprint('main', __name__)

# Routes
@main.route('/')
@main.route('/pages/')
@main.route('/pages/index')
def root():
    return render_template('pages/index.html')

@main.route('/pages/corporate')
def corporate():
    return render_template('pages/corporate.html')


