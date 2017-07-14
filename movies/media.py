import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    #Movie ratings values that would be considered valid.

    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NR", "AO"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.story = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Method to open a browser window to display the movie trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
