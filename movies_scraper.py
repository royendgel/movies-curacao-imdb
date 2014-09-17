import urllib2
import imdb
from bs4 import BeautifulSoup
connection = imdb.IMDb()
def get_rating(title, year=""):
    try:
        s_result = connection.search_movie(title + str(year))
        first_movie = s_result[0]
        connection.update(first_movie)
        return first_movie['rating']
    except:
        return 'Rating not available'

def movies_scrape():
    list = []
    url = 'http://www.themoviescuracao.com/'
    html = urllib2.urlopen(url).read()
    scrape = BeautifulSoup(html)
    for item in  scrape.select('#schedule li'):
        try:
            it = item.select('h2')[0]
            list.append({
                'Movie' : it.text,
                'rating' : get_rating(it.text, year=2014),
            })
        except Exception, e:
            print "%s %s" %("problem ", e)
    return list