import requests
from flask import Flask, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    news = requests.get('http://localhost:8000/news')
    news = news.json()

    categories = requests.get('http://localhost:8000/categories')
    categories = categories.json()

    return render_template('index.html', categories=categories, news=news)