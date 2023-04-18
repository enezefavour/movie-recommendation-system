from flask import Flask
from flask import render_template, request
import bz2
import pickle
import requests

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(bz2.BZ2File('similarity.pbz2', 'rb'))
app = Flask(__name__)


TMDB_API="https://api.themoviedb.org/3/movie/"


def recommend(movie_title):
    movies_match = movies[movies.apply(lambda row: row.astype(str).str.contains(movie_title, case=False).any(), axis=1)]
    movie_ids = movies_match.movieId.values[0]

    sorted_similar_movie = sorted(list(enumerate(similarity[movie_ids])), key=lambda x: x[1], reverse=True)
    recommended_movies = []

    for movie in sorted_similar_movie:

        try:
            movie_id = movie[0]

            if not movies[movies.movieId == movie_id].empty:
                rows = movies[movies.movieId == movie_id]
                indexed_movies = rows.values[0]
                recommended_movies.append(indexed_movies)

        except Exception as e:
            print(e)
            return e.__str__()
        
    return recommended_movies

def fetch_movie_details(recommended_movies):
    movies = []
    # print(list_of_movie_ids)

    for movie in recommended_movies:
        r = requests.get(url = TMDB_API + str(movie[0]), params = {"api_key": "37c95fe4140c4e624ee1c60b16eade3d"})
        response = r.json()
        print(response)
        if r.status_code == 200:
            movies.append(response)
        # else:
        #     movies.append({"id": movie[0], "title": movie[1], "poster_path": ""})

    return movies


@app.get("/")
def index():
    return render_template('index.html', title='Movie Recommendation System')


@app.post('/recommendation')
def post_recommendation():
    movie_list = movies['title'].values
    status = False

    try:
        if request.form:
            movies_title = request.form['search'].lower()

            status = True
            movies_ids = recommend(movies_title)

            recommended_movies= fetch_movie_details(movies_ids[0:12])

            return render_template("index.html", recommendations = recommended_movies, movie_list = movie_list, status = status)

    except Exception as e:
        error = {'error': e.__str__()}
        return error