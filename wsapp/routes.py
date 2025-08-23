# wsapp/routes.py

from flask import Blueprint, render_template, session, redirect, request, url_for, current_app
from datetime import datetime
import json
import os

# Create a blueprint named 'main'
main = Blueprint('main', __name__)

# Load JSON content for both languages
def load_content(lang):
    folder = os.path.join(current_app.root_path, 'content')
    filename = 'en.json' if lang == 'en' else 'el.json'
    path = os.path.join(folder, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
# Ensure default language
@main.before_app_request
def set_default_language():
    if 'lang' not in session:
        session['lang'] = 'el'

# ---- LANGUAGE ROUTE ----
@main.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['el', 'en']:
        session['lang'] = lang
    # Redirect back to the page that sent the request, or home
    return redirect(request.referrer or url_for('main.index'))

# ---- CONTEXT PROCESSOR ----
@main.app_context_processor
def inject_globals():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    return {
        'footer_left': content['footer']['footer_left'],
        'footer_right': content['footer']['footer_right'],
        'navbar': content['navbar'],
        'current_year': datetime.now().year
    }


# ---- PAGES ----
@main.route('/')
@main.route('/pages/')
@main.route('/pages/index')
def index():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    print(content)
    return render_template('pages/index.html', content=content['index'], navbar=content['navbar'])

@main.route('/pages/about_me')
@main.route('/pages/about_me.html')
def about_me():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    print(content)
    return render_template('pages/about_me.html', content=content['about_me'], navbar=content['navbar'])

@main.route('/pages/private')
@main.route('/pages/private.html')
def private():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    return render_template('pages/private.html', content=content['private'], navbar=content['navbar'])

@main.route('/pages/corporate')
@main.route('/pages/corporate.html')
def corporate():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    return render_template('pages/corporate.html', content=content['corporate'], navbar=content['navbar'])


@main.route('/pages/useful_links')
@main.route('/pages/useful_links.html')
def useful_links():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    return render_template('pages/useful_links.html', content=content['useful_links'], navbar=content['navbar'])


@main.route('/pages/contact')
@main.route('/pages/contact.html')
def contact():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    return render_template('pages/contact.html', content=content['contact'], navbar=content['navbar'])


@main.route('/pages/privacy_policy')
@main.route('/pages/privacy_policy.html')
def privacy_policy():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    return render_template('pages/privacy_policy.html', content=content['privacy_policy'], navbar=content['navbar'])
