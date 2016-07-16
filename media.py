__author__ = 'martin'


import webbrowser


class Movie():
    '''This Class store movie related information and
provides a way of creating a multiple instances of
that class. The __init__ method is roughly what represents
a constructor - it creates space in memory
for new instances.
The function show_trailer (instance method) open a
browser and play the trailer of a movie.
    '''

    def __init__(self,title, movie_tiles,
                 movie_poster_image, movie_trailer,
                 movie_budget, movie_genre, movie_release_date,
                 movie_director, movie_writer, movie_stars):
        self.title = title
        self.storyline = movie_tiles
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer
        self.budget = movie_budget
        self.genre = movie_genre
        self.release = movie_release_date
        self.director = movie_director
        self.writer = movie_writer
        self.stars = movie_stars


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
