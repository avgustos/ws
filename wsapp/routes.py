# wsapp/routes.py

from flask import Blueprint, render_template, session, redirect, request, url_for

# Create a blueprint named 'main'
main = Blueprint('main', __name__)

translations = {
    "el": {
        "about_me": "Ποιος Είμαι",
        "private": "Ιδιώτες",
        "corporate": "Επιχειρήσεις",
        "useful_links": "Χρήσιμοι Σύνδεσμοι",
        "contact": "Επικοινωνία",
        "new_page": "Νέα Σελίδα",
        "language": "Ελληνικά"
    },
    "en": {
        "about_me": "About Me",
        "private": "Private",
        "corporate": "Corporate",
        "useful_links": "Useful Links",
        "contact": "Contact",
        "new_page": "New Page",
        "language": "English"
    }
}

# Inject t globally into all templates (so I don’t need to add t=translations[current_lang] in every single route)
@main.app_context_processor
def inject_translations():
    current_lang = session.get('lang', 'el')  # get current language from session
    return {
        't': translations[current_lang],       # make t available in all templates
        'lang': current_lang                   # optional: current language too
    }


# ---- LANGUAGE ROUTE ----
@main.route('/set_language/<lang>')
def set_language(lang):
    if lang in ['el', 'en']:
        session['lang'] = lang
    # Redirect back to the page that sent the request, or home
    return redirect(request.referrer or url_for('main.index'))

# ---- PAGES ----
@main.route('/')
@main.route('/pages/')
@main.route('/pages/index')
def index():
    current_lang = session.get('lang', 'el')
    return render_template('pages/index.html', lang=current_lang)
@main.route('/pages/about_me')
@main.route('/pages/about_me.html')
def about_me():
    current_lang = session.get('lang', 'el')
    return render_template('pages/about_me.html', lang=current_lang)

@main.route('/pages/private')
@main.route('/pages/private.html')
def private():
    current_lang = session.get('lang', 'el')
    return render_template('pages/private.html', lang=current_lang)


@main.route('/pages/corporate')
@main.route('/pages/corporate.html')
def corporate():
    current_lang = session.get('lang', 'el')
    return render_template('pages/corporate.html', lang=current_lang)


@main.route('/pages/useful_links')
@main.route('/pages/useful_links.html')
def useful_links():
    current_lang = session.get('lang', 'el')
    return render_template('pages/useful_links.html', lang=current_lang)


@main.route('/pages/contact')
@main.route('/pages/contact.html')
def contact():
    current_lang = session.get('lang', 'el')
    return render_template('pages/contact.html', lang=current_lang, t=translations[current_lang])  # pass dictionary

