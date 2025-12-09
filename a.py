from flask import Flask , render_template , jsonify
import json
import random

app = Flask(__name__)

def load_movies():
    with open("movies.json","r") as f:   
     return json.load(f)

@app.route('/')
def dashboard():
    movie= load_movies()[:6]
    return render_template("dashboard.html", movie=movie)

@app.route('/recommender')
def index():
   return render_template("index.html")

@app.route('/recommend')
def recommend():
    movies=load_movies()
    
    select_movie=random.choice(movies)
    return jsonify(select_movie)
    
if __name__ == '__main__':
    app.run()