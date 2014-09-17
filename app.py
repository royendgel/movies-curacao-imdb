from flask import Flask
from flask import jsonify
from flask import render_template
from flask import Response

from movies_scraper import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('info.html')

@app.route('/all')
def serve_json():
    """
    Scrape movies on : http://www.themoviescuracao.com
    Take each title from movies and queries the imdb for rating.

    :return: json
    """

    return jsonify(movies_scrape())

@app.route('/realtime')
def serve_json_realitime():
    """
    Scrape movies on : http://www.themoviescuracao.com
    Take each title from movies and queries the imdb for rating.

    :return: json
    """
    def test():
        yield '{\n'
        for x in get_movie_list():
            yield '{\n'
            yield "   %s : %s,\n" %('movie', str(x))
            yield "   %s : %s,\n" %("rating", get_rating(x))
            yield '\n},'

        yield '\n}'

    # return Response(direct_passthrough=True, response=movies_scrape_generator(), content_type='application/json')
    return Response(direct_passthrough=True, response=test(), content_type='application/json')

@app.route('/s/<search>')
def search_movie(search):
    return jsonify({
        "movie" : search,
        "rating" : get_rating(search)
    })

if __name__ == "__main__":
    app.run(debug=True)