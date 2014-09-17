from flask import Flask
from flask import jsonify
from flask import Response

from movies_scraper import *
app = Flask(__name__)

@app.route('/')
def serve_json():
    """
    Scrape movies on : http://www.themoviescuracao.com
    Take each title from movies and queries the imdb for rating.

    :return: json
    """

    return jsonify(movies_scrape())

@app.route('/<search>')
def search_movie(search):
    return jsonify({
        "movie" : search,
        "rating" : get_rating(search)
    })

if __name__ == "__main__":
    app.run(debug=True)