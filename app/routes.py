from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorites')
def favorites():
    favorites = ['baseball', 'football', 'basketball', 'rugby', 'mma']
    return render_template('favorites.html')