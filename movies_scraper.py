import urllib2
import imdb
from bs4 import BeautifulSoup
def get_rating(title, year=""):
    try:
        connection = imdb.IMDb()
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
            print it
            list.append({
                'Movie' : it.text,
                'rating' : get_rating(it.text, year=2014),
            })
        except Exception, e:
            print "%s %s" %("problem ", e)
    return list

def get_movie_list():
    list = []
    url = 'http://www.themoviescuracao.com/'
    html = urllib2.urlopen(url).read()
    scrape = BeautifulSoup(html)
    for item in  scrape.select('#schedule li'):
        try:
            it = item.select('h2')[0]
            list.append(it.text)
        except:
            pass
    return list


def movies_scrape_generator():
    list = []
    url = 'http://www.themoviescuracao.com/'
    html = urllib2.urlopen(url).read()
    scrape = BeautifulSoup(html)
    for item in  scrape.select('#schedule li'):
        try:
            it = item.select('h2')[0]
            yield list.append({
                'Movie' : it.text,
                'rating' : get_rating(it.text, year=2014),
            })
        except Exception, e:
            print "%s %s" %("problem ", e)