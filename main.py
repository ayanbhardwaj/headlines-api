from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import requests
import os

API_KEY = os.environ.get("NEWS_KEY")
URL = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}"
URL_2 = f"https://newsapi.org/v2/top-headlines?country=au&apiKey={API_KEY}"

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    response = requests.get(url=URL)
    all_news = response.json()["articles"]
    return render_template("index.html", all_news=all_news)


@app.route('/au')
def aus():
    response = requests.get(url=URL_2)
    all_news = response.json()["articles"]
    return render_template("aus_news.html", all_news=all_news)


if __name__ == "__main__":
    app.run(debug=True)
