"""This defines a class called 'Movie' used to initialize a movie."""
import webbrowser
class Movie():
    """This defines class 'Movie' used to initialize a movie."""

    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        """
        This is used to create a movie instance and initialize the information of the movie such as title, storyline, poster and trailer.

        Parameters:
            movie_title - the title of the movie
            movie_storyline - the storyline of the movie
            poster_image - the poster of the movie, store as an URL
            trailer_youtube - the trailer of the movie, store as an URL from youtube
        """
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
