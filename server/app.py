from flask import Flask
from flask import render_template
import bz2
import pickle
import _pickle as cPickle
import json

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html', title='Movie Recommendation System')

@app.get('/movies')
def get_movies():
    pikd = open('movies.pkl', "rb")
    data = pickle.load(pikd)
    pikd.close()

    return {
        "status": 'success',
        "data": json.dumps(data)
    }