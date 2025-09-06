# wsapp/routes.py

from flask import Blueprint, render_template, session, redirect, request, url_for, current_app, flash
from datetime import datetime
import json
import os
from flask_mail import Message
from . import mail  # make sure mail is initialized in __init__.py

main = Blueprint('main', __name__)

# Load JSON content for both languages
def load_content(lang):
    folder = os.path.join(current_app.root_path, 'content')
    filename = 'en.json' if lang == 'en' else 'el.json'
    path = os.path.join(folder, filename)
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

# ---- LANGUAGE ROUTE ----
@main.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['el', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('main.index'))

# ---- CONTEXT PROCESSOR ----
@main.app_context_processor
def inject_globals():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    return {
        'about_me': content['footer']['about_me'],
        'privacy_policy': content['footer']['privacy_policy'],
        'cookies_policy': content['footer']['cookies_policy'],
        'navbar': content['navbar'],
        'cookies': content['cookies'],   # <-- added this
        'current_year': datetime.now().year
    }

# ---- PAGES ----
@main.route('/')
@main.route('/pages/')
@main.route('/pages/index')
def index():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    return render_template('pages/index.html', content=content['index'], navbar=content['navbar'])

@main.route('/pages/about_me')
@main.route('/pages/about_me.html')
def about_me():
    lang = session.get('lang', 'el')
    content = load_content(lang)
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

# ---- CONTACT PAGE (GET + POST) ----
@main.route('/pages/contact', methods=['GET', 'POST'])
@main.route('/pages/contact.html', methods=['GET', 'POST'])
def contact():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    
    # Get bilingual flash messages
    messages_text = content.get('contact_messages', {})
    success_msg = messages_text.get('success', "Message sent successfully!")
    error_msg = messages_text.get('error', "Error sending message.")
    fill_msg = messages_text.get('fill_all', "Please fill out all fields.")

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message_text = request.form.get('message')

        if not (name and email and message_text):
            flash(fill_msg, "danger")
            return redirect(url_for('main.contact'))

        # Compose and send email
        msg = Message(
            subject=f"New Contact Form Message from {name}",
            sender='g.mavridis@yahoo.gr',  # you can also use MAIL_DEFAULT_SENDER
            recipients=['g.mavridis@yahoo.gr'],  # your receiving email
            body=f"From: {name} <{email}>\n\n{message_text}"
        )

        try:
            mail.send(msg)
            flash(success_msg, "success")
        except Exception as e:
            flash(f"{error_msg} ({e})", "danger")

        return redirect(url_for('main.contact'))

    # GET request
    return render_template('pages/contact.html', content=content['contact'], navbar=content['navbar'])


@main.route('/pages/privacy_policy')
@main.route('/pages/privacy_policy.html')
def privacy_policy():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    return render_template('pages/privacy_policy.html', content=content['privacy_policy'], navbar=content['navbar'])

@main.route('/pages/cookies_policy')
@main.route('/pages/cookies_policy.html')
def cookies_policy():
    lang = session.get('lang', 'el')
    content = load_content(lang)
    return render_template('pages/cookies_policy.html', content=content['cookies_policy'], navbar=content['navbar'])
