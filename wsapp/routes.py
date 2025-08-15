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

@main.route('/pages/private')
@main.route('/pages/private.html')
def private():
    return render_template('pages/private.html')

@main.route('/pages/corporate')
@main.route('/pages/corporate.html')
def corporate():
    return render_template('pages/corporate.html')

@main.route('/pages/useful_links')
@main.route('/pages/useful_links.html')
def useful_links():
    return render_template('pages/useful_links.html')



